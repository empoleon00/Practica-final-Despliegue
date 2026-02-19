# Practica-final-Despliegue
# Render-Vercel

Para empezar esta práctica, empezaremos por implementar el backend a render seleccionando nuestro repositorio de github
<img width="1906" height="749" alt="image" src="https://github.com/user-attachments/assets/04f76efa-710b-4e2d-ba9f-39855939d730" />


Luego seleccionamos las siguientes opciones y creamos el servicio web:
<img width="1919" height="905" alt="image" src="https://github.com/user-attachments/assets/bc2713cc-50de-474f-8892-9acf8da84798" />


Ya tendríamos acceso al backend a traves de un enlace que nos dan:
<img width="689" height="178" alt="image" src="https://github.com/user-attachments/assets/81f639b0-f44b-44bb-ad0c-04adb6717534" />


El siguiente paso es pillar el deployhook en ajustes
<img width="1141" height="187" alt="image" src="https://github.com/user-attachments/assets/deb97b45-32c2-4361-b99f-917be84f92a9" />


Pegamos el deployhook en github en el apartado de secret and variables en action
<img width="1584" height="704" alt="image" src="https://github.com/user-attachments/assets/6195b88d-1568-41a7-9d8c-9a69826873aa" />


El siguiente paso es desplegar el frontend en vercel en add new y en proyect e importamos nuestro repositorio
<img width="967" height="671" alt="image" src="https://github.com/user-attachments/assets/031831f3-5f7a-4058-b285-5bef8eda83f4" />


Ponemos los siguientes ajustes:
<img width="577" height="902" alt="image" src="https://github.com/user-attachments/assets/b4404c61-c7a3-42af-8ad0-e1f92bb6d516" />


Una vez creado, ya tenemos acceso al frontend a través del enlace que nos proporcionan:
<img width="1918" height="971" alt="image" src="https://github.com/user-attachments/assets/e12d1023-caba-484e-91a2-4797e5f368f4" />


En ajustes, tokens creamos el siguiente token:
<img width="1122" height="400" alt="image" src="https://github.com/user-attachments/assets/794b6358-d693-4302-b553-5cd0a68afae1" />


Creamos otro token en github y lo implementamos
<img width="1579" height="711" alt="image" src="https://github.com/user-attachments/assets/b0866f59-8b24-4e3f-8010-d8d8c0906e77" />


Si hacemos un push a la rama main automaticamente en la parte de Action podemos ver como se hace un deploy en las 2 páginas
<img width="1918" height="521" alt="image" src="https://github.com/user-attachments/assets/600f3a36-4195-473c-a639-169c64d8c328" />
