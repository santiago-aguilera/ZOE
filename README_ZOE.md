
# ZOE – Gestión Documental IB  

Sistema web en desarrollo para la **gestión documental del Bachillerato Internacional (IB)**.  
El proyecto busca **organizar, almacenar y consultar evidencias académicas y proyectos** de estudiantes, docentes y coordinadores, dentro de un entorno institucional moderno, fluido y visualmente atractivo.  

---

## Maquetamientos actuales  

### Página de Inicio  
Presenta la identidad del sistema **ZOE – IB**, con un diseño moderno y responsivo.  

- **Navbar animado** con fondo en gradiente rosado-violeta.  
- **Botón de acceso** al sistema.  
- **Sección de bienvenida** explicando el propósito del sistema.  
- **Footer institucional** con enlaces, redes y créditos.  

---

### Panel Estudiante  
Espacio principal de trabajo para el **rol de estudiante IB**.  

Incluye:  
- **Calendario compacto** con vista mensual y desplazamiento fluido.  
- **Ventana emergente centrada** con el nombre del usuario y la opción de cerrar sesión.  
- **Diseño en gradiente y fondo oscuro con acentos rosados.**  
- **Interactividad natural y animaciones suaves.**  

---

### Estilo Global  
Define la identidad visual del sistema ZOE:  
- Colores principales: tonos **rosados**, **violetas** y **negros azulados**.  
- **Sombras y transparencias** que añaden profundidad.  
- **Tipografía sans-serif moderna y legible.**  
- **Diseño responsive** adaptable a todos los dispositivos.  

---

## Paleta y clases de diseño  

###  Colores principales  
```css
:root {
  --gradient: linear-gradient(90deg, #ff80bf, #b57aff);
  --bg: #0f0f1a;          /* Fondo oscuro general */
  --card: #1c1c2e;        /* Fondo de tarjetas */
  --text: #ffffff;        /* Texto principal */
  --accent: #b57aff;      /* Acento rosado-violeta */
  --muted: #e6d9f7;       /* Tonos secundarios suaves */
}
```

###  Clases principales  
| Clase | Descripción |  
|-------|--------------|  
| `.navbar` | Barra superior con fondo gradiente, logo y acceso de usuario. |  
| `.user-menu` | Contenedor del botón que muestra la ventana emergente del usuario. |  
| `.popup` | Ventana centrada para mostrar información de sesión y botón de cierre. |  
| `.calendar-container` | Contenedor del calendario mensual compacto. |  
| `.footer` | Pie de página institucional con enlaces y gradiente. |  
| `.fade-in` | Elementos con animación de aparición progresiva. |  

---

##  Scripts y funcionamiento  

Los **scripts JavaScript** son el núcleo de la interactividad del sistema.  
A continuación se explican sus funciones como si fuese una clase práctica para desarrolladores o nuevos colaboradores.  

---

###  1. Ventana emergente del usuario  

**Función:** Mostrar una ventana centrada con el nombre del usuario y la opción de cerrar sesión.  

```javascript
const userButton = document.querySelector('.user-menu button');
const popup = document.querySelector('.popup');

userButton.addEventListener('click', () => {
  popup.classList.toggle('active');
});
```

#### Explicación paso a paso:
1. Se selecciona el botón del menú del usuario (`.user-menu button`).  
2. Al hacer clic, se alterna la clase `.active` del contenedor `.popup`.  
3. Esta clase cambia la visibilidad del popup mediante CSS, mostrándolo centrado en la pantalla.  

####  Aplicación CSS:
```css
.popup {
  display: none;
  position: fixed;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  background: var(--gradient);
  color: var(--text);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 0 15px rgba(0,0,0,0.4);
  text-align: center;
  z-index: 1000;
}
.popup.active {
  display: block;
}
```

#### Resultado:
- Clic en el botón → aparece el popup.  
- Clic de nuevo → desaparece.  
- Mantiene la estética institucional con fondo degradado.  

---

### 2. Calendario compacto mensual  

**Función:** Mostrar el calendario del mes actual con los días correctamente distribuidos y un diseño compacto.  

```javascript
const date = new Date();
const renderCalendar = () => {
  const monthDays = document.querySelector('.days');
  const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
  const firstDayIndex = new Date(date.getFullYear(), date.getMonth(), 1).getDay();

  const months = [
    "Enero","Febrero","Marzo","Abril","Mayo","Junio",
    "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
  ];

  document.querySelector('.date h1').innerText = months[date.getMonth()];
  document.querySelector('.date p').innerText = date.toDateString();

  let days = "";

  for (let x = firstDayIndex; x > 0; x--) {
    days += `<div class="prev-date"></div>`;
  }

  for (let i = 1; i <= lastDay; i++) {
    days += `<div>${i}</div>`;
  }

  monthDays.innerHTML = days;
};
renderCalendar();
```

#### Explicación:
1. Se obtiene la fecha actual con `new Date()`.  
2. Se calculan el primer y último día del mes.  
3. Se construye dinámicamente el calendario con bucles.  
4. Se inserta en el DOM dentro del contenedor `.days`.  

####  Aplicación CSS:
```css
.calendar {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1rem;
  padding: 1rem;
  color: var(--text);
  text-align: center;
  box-shadow: 0 0 15px rgba(0,0,0,0.3);
}
.days div {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  line-height: 2rem;
  margin: 0.25rem;
  border-radius: 0.5rem;
  transition: 0.3s;
}
.days div:hover {
  background: var(--accent);
  color: #fff;
}
```

####  Resultado:
- Muestra el calendario actual.  
- Compacto, centrado y con colores institucionales.  
- Suave al pasar el cursor sobre los días.  

---

### 3. Animaciones suaves de carga  

**Función:** Crear un efecto de entrada visual cuando los elementos aparecen en la pantalla.  

```javascript
document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".fade-in");
  items.forEach((item, i) => {
    setTimeout(() => {
      item.classList.add("visible");
    }, i * 150);
  });
});
```

####  Explicación:
1. Se espera a que todo el DOM cargue (`DOMContentLoaded`).  
2. Selecciona todos los elementos con `.fade-in`.  
3. Los hace visibles progresivamente aplicando un retardo (`setTimeout`).  

####  Aplicación CSS:
```css
.fade-in {
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.6s, transform 0.6s;
}
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}
```

####  Resultado:
Los componentes aparecen con una **transición fluida**, mejorando la percepción profesional del sistema.

---

##  Guía práctica  

###  Cómo visualizarlo en Visual Studio Code  

1. Abre Visual Studio Code.  
2. Crea una carpeta llamada `ZOE`.  
3. Agrega dentro los archivos HTML, CSS y JS.  
4. Abre `index.html` con el **Live Server** (extensión recomendada).  
5. Explora:  
   - Navbar y footer con gradiente.  
   - Popup del usuario.  
   - Calendario funcional.  

---

##  Futuro del proyecto  

| Módulo | Descripción |  
|---------|--------------|  
| **Autenticación real** | Con base de datos y roles dinámicos. |  
| **Subida de evidencias IB** | Archivos por curso, asignatura, CAS, TOK y EE. |  
| **Panel docente** | Seguimiento, revisiones y comentarios. |  
| **Reportes PDF/Excel** | Exportación de progreso. |  
| **Notificaciones inteligentes** | Fechas límite y recordatorios. |  

---

## Tecnologías utilizadas  

- **HTML5**  
- **Tailwind CSS / CSS personalizado**  
- **JavaScript (ES6)**  
- **Diseño responsive con Flexbox y Grid**  

---
