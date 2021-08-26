# API IA Diabetes
API que consume modelo entrenado con inteligencia artificial y lo expone para ser consumido y generar predicciones de diabetes. Esto es un ejercicio académico y no un estudio médico, por lo que no puede ser tomado como referencia de salud.

URL asumiendo que se levanta el local

URL: http://127.0.0.1:12345/predict

Datos de ejemplo por postman para tener resultado "Sin Diabetes", para pruebas

[[217,75,54,4,20,0,67,187,72,0.89]]

Cada columna representa

cholesterol: Colesterol. Medido en miligramos (mg) por cada decilitro (dl) de sangre.

glucose: Glucosa. Medido en miligramos (mg) por cada decilitro (dl) de sangre.

hdl_chol: Lipoproteínas de alta densidad. Medido en miligramos (mg) por cada decilitro (dl) de sangre.

chol_hdl_ratio: Proporcion entre el colesterol y el HDL

age: Edad del paciente

gender: Sexo del paciente

bmi: Body mass index, Indice de masa corporal. Medido en kg/m^2

systolic_bp: Presión arterial sistólica. Medido en milímetros de mercurio o mmHg

diastolic_bp: Presión arterial diastólica. Medido en milímetros de mercurio o mmHg

waist_hip_ratio: Proporcion entre la cintura y la cadera

