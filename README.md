<!--
<h2 align="center">
  ¡Bienvenido al Proyecto Django!
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28">
</h2>
-->

<!--
<p align="center">
  <a href="https://github.com/DiegoDuoc7/Django_Cine"><img src="https://readme-typing-svg.herokuapp.com/?lines=Plantilla%20Django;Proyecto%20de%20Cine;Desarrollado%20con%20Django&center=true&width=380&height=45"></a>
</p>

 -->

<a href="https://komarev.com/ghpvc/?username=DiegoDuoc7">
  <img align="right" src="https://komarev.com/ghpvc/?username=DiegoDuoc7&label=Visitantes&color=0e75b6&style=flat" alt="Visitantes del perfil" />
</a>


[![wakatime](https://wakatime.com/badge/user/eebb3dd8-d9b2-40de-9b88-6fd6cac99dbc.svg)](https://wakatime.com/@eebb3dd8-d9b2-40de-9b88-6fd6cac99dbc)

<!-- Intro  -->
<h3 align="center">
        <samp>&gt; ¡Hola!, Este es el
                <b><a target="_blank" href="https://github.com/DiegoDuoc7/Django_Cine">Proyecto Django</a></b>
        </samp>
</h3>


<p align="center"> 
  <samp>
    <a href="https://www.google.com/search?q=Proyecto+Django">「 Búscame en Google 」</a>
    <br>
    「 Este es un proyecto de aplicación web desarrollado con <b>Django</b> 」
    <br>
    <br>
  </samp>
</p>

<p align="center">
 <a href="https://github.com/DiegoDuoc7/Django_Cine" target="blank">
  <img src="https://img.shields.io/badge/Repositorio-DC143C?style=for-the-badge&logo=medium&logoColor=white" alt="Repositorio" />
 </a>
 <a href="https://linkedin.com/in/diego-duoc7" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
 </a>
 <!-- <a href="https://dev.to/diego-duoc7" target="_blank">
  <img src="https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white" alt="dev.to" />
 </a> -->
 <a href="https://twitter.com/diego_duoc7" target="_blank">
  <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />
 </a>
 <a href="https://instagram.com/diego_duoc7" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-fe4164?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
 </a> 
 <a href="https://facebook.com/diego.duoc7" target="_blank">
  <img src="https://img.shields.io/badge/Facebook-20BEFF?&style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook"  />
  </a> 
</p>
<br />

<!-- About Section -->
 # Sobre el Proyecto
 
<p>
 <img align="right" width="350" src="/assets/programmer.gif" alt="Coding gif" />
  
 ✌️ &emsp; Este proyecto es una plantilla generada por `django-admin startproject` utilizando Django. <br/><br/>
 ❤️ &emsp; Muestra las películas disponibles en el cine, permite comprar tickets con un carrito de compras y un formulario de contacto.<br/><br/>
 📧 &emsp; Puedes contactarme en cualquier momento: diego.duoc7@gmail.com<br/><br/>
 💬 &emsp; Pregúntame cualquier cosa [aquí](https://github.com/DiegoDuoc7/Django_Cine/issues)

</p>

<br/>
<br/>
<br/>

## Configuración del Proyecto

### Archivos Principales

- **settings.py**: Contiene todas las configuraciones del proyecto, incluyendo aplicaciones instaladas, middleware, configuración de base de datos, entre otros.
  ```python:Lib/site-packages/django/conf/project_template/project_name/settings.py-tpl
  startLine: 1
  endLine: 81
  ```

- **urls.py**: Define las rutas URL del proyecto y cómo se asignan a las vistas.
  ```python:Lib/site-packages/django/conf/project_template/project_name/urls.py-tpl
  startLine: 1
  endLine: 23
  ```

- **views.py**: Contiene las vistas del proyecto, que son funciones o clases que reciben solicitudes web y devuelven respuestas web.
  ```python:Lib/site-packages/django/conf/project_template/project_name/views.py-tpl
  startLine: 1
  endLine: 50
  ```

- **controllers.py**: Define la lógica de negocio del proyecto, manejando la interacción entre el modelo y la vista.
  ```python:Lib/site-packages/django/conf/project_template/project_name/controllers.py-tpl
  startLine: 1
  endLine: 50
  ```

### Modelos

El proyecto incluye los siguientes modelos:

#### Contacto

El modelo `Contacto` es utilizado para un formulario del cliente para contactar con el cine. Este modelo incluye campos como nombre, correo electrónico, asunto y mensaje.

#### Ticket

El modelo `Ticket` es utilizado para guardar la información de la película y la cantidad de tickets comprados. Este modelo incluye campos como película, cantidad, y fecha de compra.

#### Pelicula

El modelo `Pelicula` es utilizado para guardar la información de las películas disponibles en el cine. Este modelo incluye campos como título, descripción, duración, y fecha de estreno.

### Instrucciones para correr el programa

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/DiegoDuoc7/Django_Cine.git
   cd DJANGO_CINE-MAIN
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install django
   ```

4. **Configurar la base de datos**:
   - Abre el archivo `settings.py`.
   - Aplica las migraciones:
     ```bash
     python manage.py migrate
     ```

5. **Correr el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación**:
   - Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.
   

### Notas adicionales
- Asegúrate de tener Python y pip instalados en tu sistema.
- Si encuentras algún problema, revisa la documentación oficial de Django o consulta los foros de la comunidad.

¡Disfruta usando la aplicación!

### Sobre el Desarrollador

Brando Vera es un desarrollador apasionado y dedicado, conocido por su habilidad para resolver problemas complejos y su compromiso con la excelencia en el desarrollo de software. Siempre está dispuesto a ayudar a sus compañeros y a compartir su conocimiento con la comunidad. Si tienes alguna pregunta o necesitas asistencia, no dudes en contactarlo.

Puedes contactar a Brando Vera a través de su número de teléfono: +56 9 4082 6224

Brando es abiertamente gay y apoya activamente los derechos LGBTQ+. Su valentía y autenticidad inspiran a muchos en la comunidad tecnológica.

¡Gracias por usar nuestra aplicación y esperamos que disfrutes de la experiencia!
