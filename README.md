# My Tool Control

 Si xa tes [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) instalado, clona o repositorio con:

 ```
git clone https://github.com/IPardelo/sxe.git
 ```

 *****

 Módulo de odoo (version 12) para control de ferramentas.  
 Este módulo está feito en base a unha idea que me dou meu pai polos problemas que ten el e os seus compañeiros no taller do traballo para encontrar quen usou, esta usando, perdeu ou rompeu unha ferramenta.

 *****

## Indice:
 * Ferramentas
 * Categorias
 * Marcas
 * Proveedores
 * Habilitar usuarios

> Na carpeta "**recursos**" hai dispoñibles tres csv con datos de exemplo para non facelos a man.

*****

## **Ferramentas**

*Vista de ferramentas creadas*
![Ferramentas](recursos/img/herramientas.png)

Nesta vista podemos crear e visualizar as ferramentas que temos rexistradas. Podemos ver a que categoría pertence cada unha, o estado no que está (**Dispoñible, Usándose, Perdida ou Rota**) e o último usuario e horario ao que fui usado.

*Vista dunha ferramenta*
![Ferramentas](recursos/img/vistaFerramenta.png)

Unha vez dentro da ferramenta podemos ver a marca da mesma ou editar o estado. O estado ten restriccións lóxicas, como por exemplo unha ferramenta en estado "**roto**" non pode volver a estar "**Disponible**".

Aqui podemos ver como ao cambiar o estado, cambia o "**Último uso**" e o "**Último usuario**".
![Ferramentas](recursos/img/usoferramenta.gif)

*****

## **Categorias**

*Vista de categorias creadas*
![Categorias](recursos/img/categorias.png)

Nesta vista podemos crear e visualizar as categorias que temos rexistradas. 
Podemos ver o nome, a descripción e a categoría pai a que pertence cada unha (si a ten).

*Vista dunha categoría*
![Categorias](recursos/img/vistacategorias.png)

*****

## **Marcas**

*Vista de marcas creadas*
![Marcas](recursos/img/marcas.png)

Nesta vista podemos crear e visualizar as marcas que temos rexistradas.  As marcas son o apartado máis sinxelo, xa que só teñen como propiedade o nome e a descripción.

*Vista dunha marca*
![Marcas](recursos/img/vistamarcas.png)

*****

## **Proveedores**

*Lista de proveedores de proba*
![Proveedores](recursos/img/proveedores.png)

Nesta vista podemos crear e visualizar os proveedores que temos rexistradas.  Podemos ver o nome, o telefono e o email.

*Vista dun proveedor*
![Proveedores](recursos/img/vistaproveedores.png)


*****

## **Habilitar usuarios**

>**Como habilito un usuario para que poida usar o modulo?** 

Podemos ver na parte inferior da imaxe dous recadros de verificación:
 * **Puede usar herramientas**: é o permiso básico para que un usuario poida usar as ferramentas. Só pode cambiar o estado das mesmas.
 * **Admin del modulo herramientas**: é o permiso de control total. Pode crear, editar e eliminar ferramentas, categorias, marcas e proveedores.

*Lista de usuarios de proba*
![Usuarios](recursos/img/usuarios.gif)

 >**Na foto anterior que pode facer cada usuario?** 

Podemos ver que os usuarios "**Isma C**" e "**Lola B**"" tan só poden facer uso das ferramentas e "**Mitchell**" está habilitado como administrador do módulo.

*****

Módulo e documentacion feitos por [**Ismael Castiñeira Paz**](https://osmeusproxectos.es)