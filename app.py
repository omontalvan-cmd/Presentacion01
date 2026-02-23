import streamlit as st
import pandas as pd
import numpy as np
import retorno as rt

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.image("dmc.png", use_container_width=True)

opcion = st.sidebar.selectbox(
    "Menú",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# -------------------------
# HOME
# -------------------------
def mostrar_home():
    st.title("Proyecto Final – Módulo 1 de Python")

    st.write("**Estudiante:** Oscar Leonardo Montalván Villafuerte")
    st.write("**Curso / Módulo:** Programación en Python – Módulo 1")
    st.write("**Año:** 2026")

    st.markdown("---")

    st.write(
        "Aplicación desarrollada en Streamlit que integra los conceptos fundamentales "
        "de programación aprendidos en el Módulo 1: variables, condicionales, "
        "estructuras de datos, funciones, programación funcional y programación orientada a objetos."
    )

    st.markdown("### Tecnologías utilizadas")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Pandas")
    st.write("- NumPy")

# -------------------------
# EJERCICIO 1
# -------------------------
def ejercicio_1():
    st.subheader("VERIFICADOR DE PRESUPUESTO")

    presupuesto = st.number_input("Presupuesto S/.", min_value=0.0, format="%.2f")
    gasto = st.number_input("Gasto S/.", min_value=0.0, format="%.2f")

    if st.button("Evaluar presupuesto"):
        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success("✅ El gasto está dentro del presupuesto.")
        else:
            st.warning("⚠️ El gasto excede el presupuesto.")

        st.write(f"Diferencia: **S/ {diferencia:,.2f}**")

# -------------------------
# EJERCICIO 2
# -------------------------
if st.button("🧹 Limpiar actividades"):
    st.session_state.actividades_ej2 = []
    st.success("Actividades limpiadas")

def ejercicio_2():
    st.subheader("REGISTRO DE ACTIVIDADES")

    if "actividades_ej2" not in st.session_state:
        st.session_state.actividades_ej2 = []

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto", "Inversión"])
    presupuesto = st.number_input("Presupuesto (S/.)", min_value=0.0, format="%.2f")
    gasto_real = st.number_input("Gasto real (S/.)", min_value=0.0, format="%.2f")

    if st.button("Agregar actividad"):
        st.session_state.actividades_ej2.append({
            "Nombre": nombre,
            "Tipo": tipo,
            "Presupuesto": presupuesto,
            "Gasto real": gasto_real})
        
        st.success("Actividad registrada")

    if st.session_state.actividades_ej2:
        df = pd.DataFrame(st.session_state.actividades_ej2)
        st.dataframe(df)

        st.markdown("### Evaluación")
        for act in st.session_state.actividades_ej2:
            if act["Gasto real"] <= act["Presupuesto"]:
                st.write(f"✔️ **{act['Nombre']}** dentro del presupuesto")
            else:
                st.write(f"❌ **{act['Nombre']}** excede el presupuesto")

# -------------------------
# EJERCICIO 3
# -------------------------
def ejercicio_3():
    st.subheader("CÁLCULO DE RETORNO ESPERADO")

    nombre = st.text_input("Nombre de la inversión")
    capital = st.number_input("Capital inicial (S/.)", min_value=0.0, format="%.2f")
    tasa = st.number_input("Tasa (%)", min_value=0.0, format="%.2f")
    meses = st.number_input("Periodo (meses)", min_value=1, step=1)

    if st.button("Calcular retorno"):
        retorno = rt.interes(capital_inicial=capital, tiempo_meses=meses, tasa_interes=tasa )

        st.markdown("### Resultado")
        st.write(
            f"📈 **{nombre}** → "
            f"El interés simple es: S/ {retorno:,.2f}"
        )

# -------------------------
# EJERCICIO 4
# -------------------------
def ejercicio_4():
    st.subheader("PROGRAMACIÓN ORIENTADA A OBJETOS (POO)")


    # DEFINICIÓN DE LA CLASE
    
    class Inversion:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            return (
        f"La compra de {self.nombre} es una inversión tipo {self.tipo}, "
        f"con un presupuesto destinado de S/ {self.presupuesto:,.2f} "
        f"y un gasto por compra de S/ {self.gasto_real:,.2f}."
    )

        # OBJETOS
    
    inversiones = [
        Inversion("Acciones", "Variable", 2000, 1800),
        Inversion("Bonos del Tesoro USA", "Fijo", 1000, 1200),
        Inversion("Depósitos a Plazo", "Fijo", 3000, 2500),
        Inversion("Criptomonedas", "Variable", 1500, 1800),
    ]

    # SELECTOR DE INVERSIONES
    
    nombres = [inv.nombre for inv in inversiones]

    seleccion = st.selectbox(
        "Seleccione una inversión",
        nombres
    )

    # Buscar el objeto seleccionado
    inversion_seleccionada = next(
        inv for inv in inversiones if inv.nombre == seleccion
    )

    # MOSTRAR INFORMACIÓN
    
    st.write("### Información de la inversión")
    st.write(inversion_seleccionada.mostrar_info())

    # Evaluación del presupuesto
    if inversion_seleccionada.esta_en_presupuesto():
        st.success("✅ La inversión está dentro del presupuesto")
    else:
        st.warning("⚠️ La inversión excede el presupuesto")

# -------------------------
# NAVEGACIÓN
# -------------------------
if opcion == "Home":
    mostrar_home()
elif opcion == "Ejercicio 1":
    ejercicio_1()
elif opcion == "Ejercicio 2":
    ejercicio_2()
elif opcion == "Ejercicio 3":
    ejercicio_3()
elif opcion == "Ejercicio 4":
    ejercicio_4()