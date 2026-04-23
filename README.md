En la terminal en donde va a tener el archivo debes de poner este comando:
git clone https://github.com/Danilocerna18/MERGESORT.git && cd MERGESORT && pip install pytest && pytest Unit_TEST.py



Este módulo contiene la implementación del algoritmo *Merge Sort* junto con su respectivo archivo de pruebas unitarias. Merge Sort es un algoritmo de ordenamiento que utiliza la estrategia de divide y vencerás, lo que significa que divide el problema en partes más pequeñas, las resuelve y luego combina los resultados de forma ordenada.

En el archivo principal, se implementa la función merge_sort, la cual recibe una lista y la divide recursivamente en dos mitades hasta que cada sublista tiene un solo elemento. Luego, estas sublistas se vuelven a unir utilizando una función auxiliar llamada merge, que se encarga de combinar dos listas ordenadas en una sola lista también ordenada. Este proceso garantiza que el resultado final esté completamente ordenado.

Además, el archivo incluye un pequeño ejemplo de uso donde se define una lista de prueba, se aplica el algoritmo y se imprime tanto la lista original como la lista ordenada. Esto permite verificar de forma rápida que el algoritmo está funcionando correctamente.

Por otro lado, el archivo de pruebas unitarias está diseñado utilizando pytest y sigue el enfoque de TDD. En este archivo se definen varios casos de prueba dentro de una lista, donde cada caso contiene una lista de entrada y el resultado esperado. Luego, usando pytest.mark.parametrize, se ejecuta automáticamente la misma prueba con todos los casos definidos.

Las pruebas cubren diferentes escenarios importantes, como listas desordenadas con duplicados, listas ya ordenadas, listas en orden inverso, listas vacías, listas con un solo elemento y listas con números negativos. Esto asegura que el algoritmo funcione correctamente en distintos tipos de situaciones.

Finalmente, cada prueba verifica que el resultado de la función merge_sort sea igual al esperado utilizando un assert. También se usa .copy() para evitar modificar la lista original durante la prueba, lo cual es una buena práctica. En general, estos archivos muestran tanto la implementación del algoritmo como una forma adecuada de validarlo automáticamente.