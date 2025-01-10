1. Creacionales

Se enfocan en cómo crear objetos de manera eficiente y flexible.

    Singleton: Garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella.
    Factory Method: Proporciona una interfaz para crear objetos en una clase base, permitiendo que las subclases definan qué objetos instanciar.
    Abstract Factory: Crea familias de objetos relacionados sin especificar sus clases concretas.
    Builder: Separa la construcción de un objeto complejo de su representación final.
    Prototype: Crea nuevos objetos copiando una instancia existente.

2. Estructurales

Se centran en la composición de clases y objetos para formar estructuras más grandes.

    Adapter: Permite que clases con interfaces incompatibles trabajen juntas.
    Bridge: Separa una abstracción de su implementación para que ambas puedan evolucionar independientemente.
    Composite: Permite tratar objetos individuales y compuestos de manera uniforme (árboles jerárquicos).
    Decorator: Agrega funcionalidades a un objeto dinámicamente, sin modificar su código base.
    Facade: Proporciona una interfaz simplificada para un sistema complejo.
    Proxy: Controla el acceso a un objeto, actuando como su representante o sustituto.

3. Comportamentales

Se enfocan en la interacción y responsabilidad entre objetos.

    Observer: Define una relación uno-a-muchos entre objetos, de modo que cuando uno cambia, los otros son notificados automáticamente.
    Strategy: Permite definir una familia de algoritmos y seleccionarlos dinámicamente.
    Command: Encapsula una solicitud como un objeto, permitiendo la parametrización y el registro de operaciones.
    State: Permite que un objeto altere su comportamiento cuando su estado interno cambia.
    Template Method: Define la estructura de un algoritmo en una clase base, permitiendo que las subclases implementen detalles específicos.
    Chain of Responsibility: Pasa solicitudes a través de una cadena de manejadores hasta que uno las procese.