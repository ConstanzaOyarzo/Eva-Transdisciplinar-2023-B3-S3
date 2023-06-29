
# Eva-Transdisciplinar-2023-B3-S3


## Descripción

En el presente proyecto se crea una interfaz grafica, la cual nos permite comprender cómo funciona el trabajo mecanico y la formula que emplea.

En esta simulación se presenta un método simplificado para calcular el trabajo mecánico. En lugar de considerar el ángulo entre la fuerza y el desplazamiento, se asume que
están en la misma dirección, lo que implica que el coseno del ángulo es igual a 1.

## Trabajo mecanico

El trabajo mecánico es la transferencia de energía a través de una fuerza aplicada a un cuerpo. Se mide en joules y puede ser
positivo o negativo dependiendo de si se transfiere o se resta energía al objeto.

Siempre que se realice trabajo se deben considerar la fuerza aplicada y el movimiento debido a esa fuerza.

Es importante tener en cuenta que el trabajo solo se realiza si hay un desplazamiento del objeto en la dirección de la fuerza aplicada. Si se aplica una fuerza sobre un
objeto pero no hay movimiento o el desplazamiento es perpendicular a la dirección de la fuerza, entonces no se realiza trabajo.

### Breve historia asociada

En el siglo XVII, matemáticos como Descartes y Fermat desarrollaron el cálculo, permitiendo una comprensión más precisa del trabajo. Leibniz introdujo el término "trabajo"
en 1687. Newton, Watt y Carnot realizaron contribuciones clave en los siglos XVIII y XIX, estableciendo leyes y principios fundamentales.

### Matemática empleada

W = F * d * cos(θ), donde F es la fuerza aplicada, d es el desplazamiento y θ es el ángulo entre la fuerza y el desplazamiento.

### Como se resuelve

1.  Primero necesitas conocer la magnitud de la fuerza aplicada sobre el objeto
2.  Determina el valor numerico del desplazamiento
3.  Determina el ángulo entre la fuerza y el desplazamiento, puede ser cualquier valor entre 0° y 180°
4.  Calcula el coseno del ángulo cos(θ)
5.  Multiplica la fuerza, el desplazamiento y el coseno del ángulo

En este caso en particular el angulo es igual a 0°, por lo que su coseno es equivalente a 1

### Aplicaciones

Cada vez que se aplica una fuerza sobre un objeto y como resultado de esa fuerza se produce desplazamiento, se realiza trabajo.

1. Al levantar bolsas, empujar un mueble, patear una pelota.
2. El trabajo mecánico tambien esta presente al realizar actividades físicas. Por ejemplo, en el levantamiento de pesas,
el trabajo se realiza al elevar las pesas. Al hacer flexiones realizas trabajo contra tu propio peso.
3. Cuando un automovil adquiere rapidez, debido a la fuerza que genera el motor del mismo para impulsarlo. Por otro lado, al frenar, se aplica una fuerza en dirección
opuesta al movimiento del automóvil, por lo que tambien se realiza trabajo, pero en este caso el trabajo es negativo.

## Programación


### Descripción de las herramientas utilizadas

- tkinter: Se utiliza para crear la interfaz gráficas de usuario, crear y administrar la
ventana principal, marcos, etiquetas, botones, entradas y otros elementos.

- matplotlib: Se utiliza para crear un gráfico de trabajo mecánico.

- PIL: Se utiliza para cargar una imagen del personaje en la interfaz.

- re: Se utiliza para validar la entrada de datos en los campos de fuerza y distancia, asegurándose de que solo se ingresen valores numéricos.

- ttk: Se utiliza para crear y manejar los datos dentro de la tabla del marco 4.

- Figure y FigureCanvasTkAgg: Clases especificas de Matplotlib que se utilizan para crear, mostrar gráficos en una interfaz Tkinter y que el grafico tenga una buena calidad
de imagen.

- Image e ImageTk: Se utilizan para cargar y mostrar imágenes en la interfaz de Tkinter.

### Guia de instalación

https://www.youtube.com/watch?v=RAZG22fNBLc

[Descargar ejecutable]https://www.mediafire.com/file/et161eg3wo2gkwi/archivo+exe.rar/file

### Guia de uso

https://www.youtube.com/watch?v=vFWj80KYi44

### Explicación del código desarrollado.

https://www.youtube.com/watch?v=W3y99-_TyHg

## Conclusiones

El trabajo mecanico es una magnitud fisica que se encuentra presente en nuestra vida cotidiana, incluso sin darnos cuenta , ya que ocurre cada vez que se aplica fuerza a un
objeto y este se desplaza como resultado.

Es importante destacar que el trabajo no solo implica fuerza, sino también el desplazamiento en la dirección de esa fuerza. Si empujas un objeto pero no se mueve o el
desplazamiento es perpendicular a la dirección de la fuerza, no se está realizando trabajo.
