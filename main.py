import pandas as pd 
import os


def main():

    docentes_1_path = os.path.join(".",  "data", "input", "raw",  "docentes_1.xlsx")
    docentes_2_path = os.path.join(".",  "data", "input", "raw","docentes_2.csv")
    docentes_3_path = os.path.join(".",  "data", "input", "raw","docentes_3.parquet")

    output_solution_path = os.path.join( ".",  "data",  'solucion', 'solucion_desafio.xlsx')

    excel = pd.read_excel(docentes_1_path, sheet_name="data").drop_duplicates().dropna()
    csv = pd.read_csv(docentes_2_path, sep=";").drop_duplicates().dropna()
    parquet = pd.read_parquet(docentes_3_path).drop_duplicates().dropna()

    excel.rename(columns={'ID_DOCENTE' : 'identificador_docente', "NOMBRE_DOCENTE": "nombre_docente"}, inplace=True)
    csv.rename(columns={'id_docente' : 'identificador_docente'}, inplace=True)
    parquet.rename(columns={'idDocente' : 'identificador_docente', "nombreDocente": "nombre_docente"}, inplace=True)



    merged_data = pd.concat([excel, csv, parquet])

    merged_data['identificador_docente'] = merged_data['identificador_docente'].astype(int)

    merged_data = merged_data.sort_values(by=["identificador_docente"], ascending=True)

    merged_data = merged_data[['identificador_docente', "nombre_docente"]].drop_duplicates()
    merged_data.to_excel(output_solution_path)



if __name__ == "__main__":
    main()
