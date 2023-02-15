import threading
import time

from src.client import Client
from src.waiter import Waiter
from src.table import Table
from src.adapters.producer_rabbit import ProducerRabbitMQ


class Restaurant:
    def __init__(self, config: dict, producer: ProducerRabbitMQ) -> None:
        self.threads = []
        self.garcons = []
        self.config = config
        self.producer = producer

    def __verificar_garcom_disponivel(self)-> bool:
        return len(self.garcons) > 0 and len(self.garcons) <= self.config.get("amount_waiters")

    def __operacoes_garcom(self):
        mesa, pedidos_mesa = self.__criar_mesa_com_pessoas()

        ultimo_gacom_id = len(self.garcons) -1
        garcom = self.garcons[ultimo_gacom_id]
        garcom_id = garcom.id

        for pedido in pedidos_mesa:
            dados_pedido = pedido.get()
            order_number = dados_pedido.get("order_number")

            print(f"[x] Garçom {garcom_id} está anotando o pedido {order_number}")
            garcom.anota_pedidos(pedido, mesa)

            tempo_simbolico = 0.0002 * garcom_id
            time.sleep(tempo_simbolico)

            print(f"[x] Garçom {garcom_id} anotou o pedido {order_number}")
            print(f"[x] Garçom {garcom_id} enviou o pedido {order_number} para cozinha")
        
        garcom.enviar_pedido_cozinha()
        time.sleep(1)


    def __chamar_garcom_thread(self):
        thread_garcom = threading.Thread(target=self.__operacoes_garcom)
        self.threads.append(thread_garcom)
        thread_garcom.start()


    def __definir_garcons(self):
        for i in range(self.config.get("amount_waiters")):
            id = i + 1
            garcom = Waiter(id, self.producer)
            self.garcons.append(garcom)

    def __criar_mesa_com_pessoas(self):
        mesa = Table()

        pedidos = []

        for nome in range(self.config.get("number_people_per_table")):
            nome_cliente = "Pessoa "+ str(nome + 1)
            cliente = Client(nome_cliente)
            mesa.accommodate_customer(cliente)

            pedido = cliente.make_order([
                {
                    "produto": "X-TUDO"
                },
                {
                    "produto": "Porção de Batatas"
                }
            ])

            pedidos.append(pedido)

        return  (mesa, pedidos)


    def execute(self):
        quantidade_mesas = self.config.get("amount_tables")

        self.__definir_garcons()
        
        # Enquanto existir mesas:
        while quantidade_mesas > 0: 
            self.__criar_mesa_com_pessoas()
            
            # E Garçom disponivel então:
            if self.__verificar_garcom_disponivel():
                print("[X] Mesa N°: ", quantidade_mesas)

                # Calculos necessários
                MESA_RECEPCIONADA = 1
                quantidade_mesas -= MESA_RECEPCIONADA

                # Chamar Thread
                self.__chamar_garcom_thread()
                
                # Remova um Garçom da lista de controle
                self.garcons.pop()
            else:
                print("\n\n################################ [GARGALO] ################################")
                print(f"[GARGALO] O Restaurante está sem garçom disponiveis!")
                print("###########################################################################\n\n")


                # Percorre a lista de Threads e para cada thread da lista
                for t in self.threads:
                    t.join()

                    # Verifica se não está em execução
                    if not t.is_alive():
                        UM_GARCOM = 1

                        self.threads.remove(t)
                        proximo_garcom_id = len(self.garcons) + UM_GARCOM
                        self.garcons.append(Waiter(proximo_garcom_id, self.producer))

                        print("\n\n########################### [Liberando Garçom] ###########################")
                        print("[X] Liberando Garçom para novos pedidos")
                        print("###########################################################################\n\n")