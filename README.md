Gestión de Gastos

Una aplicación web simple construida con Flask para gestionar y repartir gastos entre personas. Ideal para llevar un registro de gastos compartidos en eventos, viajes o cualquier otra situación en la que varias personas compartan gastos.

 <!-- Puedes reemplazar esto con una imagen relevante -->
Características

    Agregar Personas: Añade personas al sistema para incluirlas en los cálculos de gastos.
    Agregar Gastos: Registra los gastos, especifica quién pagó y con quién se reparte.
    Eliminar Personas: Elimina personas del sistema y ajusta automáticamente los gastos asociados.
    Calcular Saldos: Calcula los saldos de cada persona y muestra quién le debe a quién.

Tecnologías Utilizadas

    Flask: Microframework para Python utilizado para construir la aplicación web.
    Python: Lenguaje de programación principal.
    JSON: Formato de datos utilizado para almacenar información sobre personas y gastos.

Instalación

    Clonar el Repositorio

    bash

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

Configurar el Entorno Virtual

bash

python -m venv venv
source venv/bin/activate  # Para Windows usa: venv\Scripts\activate

Instalar las Dependencias

bash

pip install -r requirements.txt

Ejecutar la Aplicación

bash

    flask run

    La aplicación estará disponible en http://127.0.0.1:5000.

Uso

    Agregar Personas
        Navega a la sección "Agregar Persona".
        Introduce el nombre de la persona y haz clic en "Agregar".

    Agregar Gastos
        Navega a la sección "Agregar Gasto".
        Introduce la cantidad gastada, selecciona el pagador y los beneficiarios.
        Haz clic en "Agregar Gasto".

    Eliminar Personas
        Navega a la sección "Eliminar Persona".
        Haz clic en el botón "Eliminar" junto al nombre de la persona que deseas eliminar.

    Ver Transacciones
        La sección "Transacciones" muestra las deudas y créditos entre personas basados en los gastos registrados.

Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue estos pasos:

    Fork el repositorio.
    Crea una nueva rama (git checkout -b feature-nueva).
    Realiza tus cambios y haz commit (git commit -am 'Añadir nueva característica').
    Push a la rama (git push origin feature-nueva).
    Abre una Pull Request.

Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
