
import time

def disparar_alerta_email(item, quantidade):
    """
    Simula o envio de um e-mail de alerta para a administração.
    Essa função é chamada unicamente quando a condição crítica é atingida.
    """
    print("\n" + "="*55)
    print("🚨 ALERTA CRÍTICO DE SISTEMA 🚨")
    print("="*55)
    print("📧 SIMULAÇÃO DE E-MAIL ENVIADO")
    print("Para: administracao@deresponsa.com.br")
    print("Assunto: AÇÃO NECESSÁRIA - Reposição de Estoque")
    print(f"Mensagem: O item '{item}' atingiu a zona crítica!")
    print(f"Quantidade disponível: {quantidade} unidades.")
    print("="*55 + "\n")

def monitorar_operacao(dados_diarios, limite_critico):
    """
    Módulo de lógica: analisa os dados e decide quando acionar o alerta.
    """
    print(f"Iniciando monitoramento... (Limite crítico: {limite_critico})\n")

    for dia, quantidade in enumerate(dados_diarios, start=1):
        print(f"Dia {dia:02d} | Estoque atual: {quantidade} unidades")

        # Lógica condicional: verifica se atingiu o ponto crítico
        if quantidade <= limite_critico:
            disparar_alerta_email("Seda Personalizada", quantidade)
            print("Monitoramento pausado. Aguardando reposição.")
            break 

        time.sleep(0.5)  # Simula o tempo de processamento entre as leituras

if __name__ == "__main__":
    # Dados simulados: queda gradual no estoque
    historico_estoque = [120, 105, 90, 70, 55, 40, 25, 12, 5, 0]
    
    # Regra de negócio: disparar alerta quando restarem 15 unidades ou menos
    limite_de_seguranca = 15
    
    monitorar_operacao(historico_estoque, limite_de_seguranca)
