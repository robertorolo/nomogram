import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

flname = sys.argv[1]

def se(c, dn, ml, ms):
    if ml/ms >= 10:
        return (c*(dn**3))/(1/ms-1/ml)
    else:
        return (c*(dn**3))/(ms)
        
def plt_size_line(dn, m_max=10**5, c=1):
    plt.plot([10**0, m_max], [se(c, dn, 10**0, 10**0), se(c, dn, m_max, m_max)], label=dn)
    
def plt_mass_red(c, dn, ml, ms):
    global s
    se0, se1 = se(c, dn, ml, ml), se(c, dn, ms, ms)
    plt.plot([ml ,ms], [se0, se1], color='black', marker='o')
    if s == 1:
        plt.annotate(s, (ml+0.1*ml, se0+0.5*se0), fontsize=10)
        s=s+1
    plt.annotate(s, (ms+0.1*ms, se1+0.5*se1), fontsize=10)
    s=s+1
    erro.append(se1)
    
def plt_size_red(c0, c1, dn0, dn1, ml, ms):
    global s
    se0, se1 = se(c0, dn0, ml, ms), se(c1, dn1, ml, ms)
    plt.plot([ml, ms], [se0, se1], color='black', marker='o')
    if s == 1:
        plt.annotate(s, (ms+0.1*ms, se0+0.5*se0), fontsize=10)
        s=s+1
    plt.annotate(s, (ms+0.1*ms, se1+0.5*se1), fontsize=10)
    s=s+1
    
protocolo = pd.read_csv(flname)

if not all(elem in protocolo.columns  for elem in ['ml', 'ms', 'dn', 'c']):
    sys.exit('Cabeçalho inválido!')
    
fig = plt.figure(figsize=(10,5))
plt.yscale('log')
plt.ylabel('Erro fundamental (σ²)', fontsize=12)
plt.yticks(fontsize=10)
plt.tick_params(axis='y', which='both', labelleft=False, labelright=True, labelsize=10)
plt.xscale('log')
plt.xlabel('Massa da amostra (g)', fontsize=12)
plt.tick_params(axis='x', which='both', labelsize=10)
plt.grid(linestyle='--', alpha=0.5, which='both')
plt.title('Protocolo de amostragem', fontsize=12)

unique_dn, indexes = np.unique(protocolo['dn'], return_index=True) 
argsort = np.flip(np.argsort(unique_dn)) 
unique_dn = unique_dn[argsort]
indexes = indexes[argsort]
for dn, idx in zip(unique_dn, indexes):
    plt_size_line(dn, m_max=10**5, c=protocolo.loc[idx, 'c'])
    
erro = []
s = 1
for idx in range(1,protocolo.shape[0]):
    if protocolo.loc[idx, 'ml'] > protocolo.loc[idx, 'ms']:
        print('Redução de massa no passo {}'.format(s))
        plt_mass_red(c=protocolo.loc[idx, 'c'], dn=protocolo.loc[idx, 'dn'], ml=protocolo.loc[idx, 'ml'], ms=protocolo.loc[idx, 'ms'])
        
    if protocolo.loc[idx, 'dn'] < protocolo.loc[idx-1, 'dn']:
        print('Redução de tamanho no passo {}'.format(s))
        plt_size_red(c0=protocolo.loc[idx-1, 'c'], c1=protocolo.loc[idx, 'c'], dn0=protocolo.loc[idx-1, 'dn'], dn1=protocolo.loc[idx, 'dn'], ml=protocolo.loc[idx, 'ml'], ms=protocolo.loc[idx, 'ms'])
        
plt.legend(bbox_to_anchor=(1.06, 1), loc='upper left', frameon=False, title='Top sizes (cm):')
texto = '''
σ²: {}
σ: {}
'''.format(round(np.sum(erro),5), round(np.sqrt(np.sum(erro)),5))

plt.annotate(texto, xycoords='axes fraction', xy=(0.02, 0), fontsize=12)

fig_name = input('Informe o nome da imagem (default: nomograma.png): ')
if fig_name == '':
    fig_name = 'nomograma'
else:
    fig_name = fig_name
plt.savefig(fig_name, facecolor='white', dpi=300, bbox_inches='tight')
print('Imagem salva como {}.png!'.format(fig_name))