## TP N°2: Software Defined Networks

Para realizar las pruebas es necesario en todos los casos primero:

    1. Ejecutar POX en una terminal, para eso se puede hacer uso de un script
        
        ```
        $ ./firewall.sh
        ```

    2. Ejecutar mininet en otra terminal con el controlador externo

        ```
        $ sudo mn --custom topology.py --topo chain,{CANTIDAD DE SWITCHES} --controller remote
        ```

    Todas las direcciones de los hosts son del tipo 10.0.0.X, donde X es el número de host que en este trabajo va del 1 al 4.

### Regla 1

En la consola de mininet abrir dos xterm, cada una con un host diferente. Para evitar que el descarte de paquetes sea a causa de la regla 3 se debe evitar usar el host 1 y el host 3 en simultáneo.

```
    mininet> xterm h1
    mininet> xterm h4
```

Elegir alguna de las dos terminales para levantar el servidor y ejecutar el comando iperf. Para probar esta regla la única condición es especificar el puerto 80. Por ejemplo si se elige h1 como servidor se debe ejecutar el siguiente comando en su xterm:

```    
    # iperf -s -p 80
```

Y en h4 como cliente el comando:

```
    # iperf -c 10.0.0.1 -p 80
```

La salida del cliente debería ser 

```
connect failed. Operation now in progress
```

### Regla 2

En la consola de mininet abrir dos xterm, cada una con un host diferente. Para evitar que el descarte de paquetes sea a causa de la regla 3 se debe evitar usar el host 1 y el host 3 en simultáneo.

```
    mininet> xterm h1
    mininet> xterm h4
```

Elegir alguna de las dos terminales para levantar el servidor y ejecutar el comando iperf. Para probar esta regla las condiciones son: 1. que el cliente sea el h1, 2. que el puerto sea el 5001, 3. que el protocolo de la capa de transporte sea UDP. Por ejemplo si se elige h4 como servidor se debe ejecutar el siguiente comando en su xterm:

```    
    # iperf -s -p 5001 -u
```

Y en h1 como cliente el comando:

```
    # iperf -c 10.0.0.4 -p 5001 -u
```

La salida esperada en cliente debería ser del estilo

```
Client connecting to 10.0.0.4, UDP port 5001
Sending 1470 byte datagrams, IPG target: 11215.21 us (kalman adjust)
UDP buffer size: 208 KByte (default)
------------------------------------------------------------
[  5] local 10.0.0.1 port 33888 connected with 10.0.0.4 port 5001
[  5] WARNING: did not receive ack of last datagram after 10 tries.
[ 11] Interval       Transfer     Bandwidth
[  5] 0.0-10.0 sec   1.25 MBytes  1.05 Mbits/sec
[  5] Sent 882 datagrams
```


### Regla 3

La única condición en este caso es que el h1 y el h3 no se puedan comunicar en ninguna de las dos direcciones. Para probarlo se ejecuta el comando pingall en la consola de mininet.

```
    mininet> pingall
```

Cuya respuesta debería ser:

```
*** Ping: testing ping reachability
h1 -> h2 X h4 
h2 -> h1 h3 h4 
h3 -> X h2 h4 
h4 -> h1 h2 h3 
*** Results: 16% dropped (10/12 received)
```

Adicionalmente se puede abrir una consola para cada host

```
    mininet> xterm h1
    mininet> xterm h3
```

Y luego en cada xterm una hacer un ping específicamente hacia el otro host, por ejemplo en h1:

```
    # ping 10.0.0.3
```

Cuya salida debería ser del estilo:

```
--- 10.0.0.3 ping statistics ---
6 packets transmitted, 0 received, 100% packet loss, time 5124ms
```

Y en h3:

```
    # ping 10.0.0.1
```

Cuya salida debería ser del estilo:

```
--- 10.0.0.1 ping statistics ---
164 packets transmitted, 0 received, 100% packet loss, time 166890ms
```