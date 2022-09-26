#ESERCIZIO 001_VLAN

Obiettivo:
    - realizzare un'unica rete divisa in due VLAN tramite l'utilizzo del metodo port based (utilizzando i numeri di porta dello switch)

- inserire 6 pc, 2 faranno parte della VLAN Robotici e 2 della VLAN Informatici.
- collegare 4 pc a uno switch e 2 ad un altro switch.
- collegare i due switch tramite l'utilizzo di un cavo cross:
        - nel caso di port based ACCES collegare i due switch tramite l'utilizzo di 2 cavi (uno per ogni VLAN)
        - nel casi di port based TRUNK collegare i due switch tramite l'utilizzo di un unico cavo su cui potranno transitare i pacchetti di entrambe le VLAN

001_acces.pkt
tramite l'utilizzo di due cavi separati collego i due switch in modo da assegnare a ognuno di essi una diversa VLAN. in questo modo quando voglio inviare dati sulla VLAN 10 il pacchetto di dati transita sul cavo collegato alle porte Fa4/1 e Fa0/1; quando voglio inviare un pacchetti sulla VLAN 20 il pacchetto transita sul cavo collegato alle porte Fa5/1 e Fa1/1 rispettivamente collegati ai due switch.



001_trunk.pkt
tramite l'utilizzo di un solo cavo di collegamento tra i due switch riesco a far comunicare le due VLAN separatamento tramite l'utilizzo di un solo cavo di collegamento. 