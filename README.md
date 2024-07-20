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
    「 Las tecnologías usadas en este proyecto son 」
    <br>
    <br>
  </samp>
</p>

<p align="center">
 <a href="https://www.python.org/" target="blank">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
 </a>
 <a href="https://www.djangoproject.com/" target="_blank">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
 </a>
 <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank">
  <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML" />
 </a>
 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
 </a> 
 <a href="https://getbootstrap.com/" target="_blank">
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"  />
 </a> 
 <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank">
  <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS"  />
 </a> 
 <a href="https://www.sqlite.org/index.html" target="_blank">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"  />
 </a> 
 <a href="https://git-scm.com/" target="_blank">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"  />
 </a> 
 <a href="https://github.com/" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"  />
 </a> 
</p>
<br />

<!-- About Section -->
 # Sobre el Proyecto
 
<p>
 <img align="right" width="350" src="/assets/programmer.gif" alt="Coding gif" />
  
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
