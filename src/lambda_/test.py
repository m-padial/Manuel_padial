import pandas as pd
from scraping import scrapeo_opciones_y_futuros
from volatilidad import calcular_volatilidad




def test_scrapeo_opciones_y_futuros():
    print("🔍 Ejecutando test_scrapeo_opciones_y_futuros...")

    df_opciones, df_futuros = scrapeo_opciones_y_futuros()

    assert isinstance(df_opciones, pd.DataFrame), "❌ df_opciones no es un DataFrame"
    assert isinstance(df_futuros, pd.DataFrame), "❌ df_futuros no es un DataFrame"

    assert not df_opciones.empty, "❌ df_opciones está vacío"
    assert not df_futuros.empty, "❌ df_futuros está vacío"

    for col in ['strike', 'put/call', 'FV']:
        assert col in df_opciones.columns, f"❌ Falta la columna '{col}' en df_opciones"

    print("✅ Test de scrapeo superado.")


def test_calculo_volatilidad():
    print(" Ejecutando test_calculo_volatilidad...")

    df_opciones, df_futuros = scrapeo_opciones_y_futuros()
    df_resultado = calcular_volatilidad(df_opciones, df_futuros)

    assert isinstance(df_resultado, pd.DataFrame), "❌ df_resultado no es un DataFrame"
    assert 'σ' in df_resultado.columns, "❌ Falta la columna 'σ' (volatilidad implícita)"
    assert df_resultado['σ'].notnull().sum() > 0, "❌ Ningún valor calculado para 'σ'"

    print(" Test de cálculo de volatilidad superado.")


if __name__ == "__main__":
    test_scrapeo_opciones_y_futuros()
    test_calculo_volatilidad()
    print(" Todos los tests se ejecutaron correctamente.")
