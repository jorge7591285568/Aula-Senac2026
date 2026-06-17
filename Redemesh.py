import networkx as nx
import matplotlib.pyplot as mpl
import random
import os

os.makedirs('output', exist_ok=True)

class RedeMesh:
    def __init__(self, nome="Rede Mesh"):
        self.nome = nome
        self.G = nx.Graph()
        self.posicoes = {}
    
    def adicionar_dispositivo(self, nome, tipo="dispositivo", posicao=None):
        self.G.add_node(nome, tipo=tipo, posicao=posicao)
        if posicao:
            self.posicoes[nome] = posicao
        print(f"Dispositivo {nome} ({tipo}) adicionado")
    
    def adicionar_conexao(self, dispositivo1, dispositivo2, distancia=None, latencia=None):
        if distancia is None:
            distancia = random.uniform(1, 10)
        if latencia is None:
            latencia = distancia * 2
        
        self.G.add_edge(dispositivo1, dispositivo2, 
                       distancia=distancia, 
                       latencia=latencia,
                       bandwidth=random.uniform(10, 100))
        print(f"Conexão entre {dispositivo1} e {dispositivo2} adicionada (distancia: {distancia:.2f})")
    
    def calcular_rotas_mesh(self, dispositivo_origem):
        rotas = {}
        
        for dispositivo_destino in self.G.nodes():
            if dispositivo_destino == dispositivo_origem:
                continue
            
            todos_caminhos = list(nx.all_simple_paths(self.G, dispositivo_origem, dispositivo_destino))
            
            if todos_caminhos:
                melhor_caminho = None
                menor_distancia = float('inf')
                
                for caminho in todos_caminhos:
                    distancia_total = 0
                    for i in range(len(caminho)-1):
                        u, v = caminho[i], caminho[i+1]
                        distancia_total += self.G[u][v]['distancia']
                    
                    if distancia_total < menor_distancia:
                        menor_distancia = distancia_total
                        melhor_caminho = caminho
                
                rotas[dispositivo_destino] = {
                    'caminho': melhor_caminho,
                    'distancia_total': menor_distancia,
                    'num_dispositivos': len(melhor_caminho),
                    'todos_caminhos': len(todos_caminhos)
                }
        
        return rotas
    
    def calcular_densidade_rede(self):
        num_dispositivos = len(self.G.nodes())
        num_conexoes = len(self.G.edges())
        
        if num_dispositivos <= 1:
            return {'densidade': 0, 'conexoes_por_dispositivo': 0}
        
        densidade = (2 * num_conexoes) / (num_dispositivos * (num_dispositivos - 1))
        
        return {
            'num_dispositivos': num_dispositivos,
            'num_conexoes': num_conexoes,
            'densidade': densidade,
            'conexoes_por_dispositivo': num_conexoes / num_dispositivos
        }
    
    def encontrar_dispositivos_criticos(self):
        criticos = []
        
        for dispositivo in self.G.nodes():
            G_temp = self.G.copy()
            G_temp.remove_node(dispositivo)
            
            # CORREÇÃO: converter gerador para lista
            if len(list(nx.connected_components(G_temp))) > 1:
                criticos.append(dispositivo)
        
        return criticos
    
    def calcular_resiliencia_rede(self):
        num_dispositivos = len(self.G.nodes())
        criticos = self.encontrar_dispositivos_criticos()
        
        resiliencia = (num_dispositivos - len(criticos)) / num_dispositivos if num_dispositivos > 0 else 0
        
        return {
            'num_dispositivos': num_dispositivos,
            'dispositivos_criticos': len(criticos),
            'criticos': criticos,
            'resiliencia': resiliencia,
            'percentual_criticos': (len(criticos) / num_dispositivos * 100) if num_dispositivos > 0 else 0
        }
    
    def visualizar_rede(self, rotas=None, dispositivo_origem=None):
        fig = mpl.figure(figsize=(14, 10))
        mpl.rcParams['font.size'] = 10
        
        pos = self.posicoes if self.posicoes else nx.spring_layout(self.G, seed=42, k=2)
        
        nx.draw_networkx_edges(self.G, pos, edge_color='gray', width=1.5, alpha=0.5)
        
        if rotas and dispositivo_origem:
            for destino, dados in rotas.items():
                caminho = dados['caminho']
                if len(caminho) > 1:
                    rotas_arestas = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
                    nx.draw_networkx_edges(self.G, pos, edgelist=rotas_arestas, 
                                         edge_color='red', width=3, alpha=0.7)
        
        nodes = list(self.G.nodes())
        cores = ['lightblue' if self.G.nodes()[n]['tipo'] == 'dispositivo' else 'lightgreen' for n in nodes]
        
        nx.draw_networkx_nodes(self.G, pos, node_color=cores, node_size=1000, 
                              edgecolors='black', linewidths=2)
        
        nx.draw_networkx_labels(self.G, pos, font_size=12, font_weight='bold')
        
        edge_labels = {}
        for u, v in self.G.edges():
            distancia = self.G[u][v]['distancia']
            latencia = self.G[u][v]['latencia']
            edge_labels[(u, v)] = f"D:{distancia:.1f} L:{latencia:.1f}"
        
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_size=8)
        
        titulo = f"{self.nome} - Rede Mesh"
        if rotas and dispositivo_origem:
            titulo += f" - Rotas de {dispositivo_origem}"
        
        mpl.title(titulo, pad=20, fontsize=16, fontweight='bold')
        mpl.tight_layout()
        
        return fig, pos
    
    def gerar_relatorio(self):
        densidade = self.calcular_densidade_rede()
        resiliencia = self.calcular_resiliencia_rede()
        
        relatorio = {
            'nome': self.nome,
            'num_dispositivos': densidade['num_dispositivos'],
            'num_conexoes': densidade['num_conexoes'],
            'densidade_rede': densidade['densidade'],
            'conexoes_por_dispositivo': densidade['conexoes_por_dispositivo'],
            'resiliencia': resiliencia['resiliencia'],
            'dispositivos_criticos': resiliencia['criticos'],
            'percentual_criticos': resiliencia['percentual_criticos']
        }
        
        return relatorio


print("=" * 60)
print(" ESTUDO DE REDES MESH - PROGRAMA DE SIMULAÇÃO")
print("=" * 60)

mesh = RedeMesh("Rede Mesh de Sensores")

print("\n1. ADICIONANDO DISPOSITIVOS:")
mesh.adicionar_dispositivo("S1", "sensor", (0, 0))
mesh.adicionar_dispositivo("S2", "sensor", (3, 0))
mesh.adicionar_dispositivo("S3", "sensor", (0, 3))
mesh.adicionar_dispositivo("S4", "sensor", (3, 3))
mesh.adicionar_dispositivo("R1", "roteador", (1.5, 1.5))
mesh.adicionar_dispositivo("S5", "sensor", (6, 1.5))
mesh.adicionar_dispositivo("S6", "sensor", (1.5, 6))

print("\n2. ADICIONANDO CONEXÕES (Topologia Mesh):")
mesh.adicionar_conexao("S1", "S2")
mesh.adicionar_conexao("S1", "S3")
mesh.adicionar_conexao("S1", "R1")
mesh.adicionar_conexao("S2", "S4")
mesh.adicionar_conexao("S2", "R1")
mesh.adicionar_conexao("S3", "S4")
mesh.adicionar_conexao("S3", "R1")
mesh.adicionar_conexao("S4", "R1")
mesh.adicionar_conexao("R1", "S5")
mesh.adicionar_conexao("R1", "S6")
mesh.adicionar_conexao("S5", "S6")

print("\n3. ANÁLISE DE DENSIDADE DA REDE:")
densidade = mesh.calcular_densidade_rede()
print(f"   Dispositivos: {densidade['num_dispositivos']}")
print(f"   Conexões: {densidade['num_conexoes']}")
print(f"   Densidade: {densidade['densidade']:.3f} ({densidade['densidade']*100:.1f}%)")
print(f"   Conexões por dispositivo: {densidade['conexoes_por_dispositivo']:.2f}")

print("\n4. ESTUDO DE ROTAS MESH (de S1 para todos):")
rotas = mesh.calcular_rotas_mesh("S1")

for destino, dados in rotas.items():
    print(f"   {destino}: {dados['caminho']}")
    print(f"      Distancia: {dados['distancia_total']:.2f}, Dispositivos: {dados['num_dispositivos']}, Caminhos possiveis: {dados['todos_caminhos']}")

print("\n5. ANÁLISE DE RESILIÊNCIA:")
resiliencia = mesh.calcular_resiliencia_rede()
print(f"  Resiliência: {resiliencia['resiliencia']:.3f} ({resiliencia['resiliencia']*100:.1f}%)")
print(f"  Dispositivos críticos: {resiliencia['dispositivos_criticos']}")
print(f"  Lista de dispositivos críticos: {resiliencia['criticos']}")
print(f"  Percentual de dispositivos críticos: {resiliencia['percentual_criticos']:.1f}%")

print("\n6. RELATÓRIO COMPLETO DA REDE:")
relatorio = mesh.gerar_relatorio()
for chave, valor in relatorio.items():
    print(f"   {chave}: {valor}")

print("\n7. VISUALIZANDO REDE:")
rotas_S1 = mesh.calcular_rotas_mesh("S1")
fig, pos = mesh.visualizar_rede(rotas=rotas_S1, dispositivo_origem="S1")

output_file = 'output/rede_mesh_estudo.png'
fig.savefig(output_file, dpi=150, bbox_inches='tight')

print(f"\nImagem salva em: {output_file}")

print(f"\n{'='*60}")
print("RESULTADOS FINAIS")
print(f"{'='*60}")
print(f"  Rede analisada: {relatorio['nome']}")
print(f"  Dispositivos: {relatorio['num_dispositivos']}")
print(f"  Conexões: {relatorio['num_conexoes']}")
print(f"  Densidade: {relatorio['densidade_rede']:.2f}")
print(f"  Resiliência: {relatorio['resiliencia']:.2f}")
print(f"  Dispositivos críticos: {relatorio['dispositivos_criticos']}")
print(f"{'='*60}")