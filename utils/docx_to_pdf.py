import os
import platform
import subprocess

from docx2pdf import convert as docx_convert


class ConvertDocxToPdf:
    def __init__(self, document_file: str, name_file_pdf: str) -> None:
        self.__document_file = document_file
        self.__name_file_pdf = name_file_pdf
        self.system = platform.system()

    def convert_to_pdf(self) -> bool:
        try:
            if not self.is_valid_document():
                print(
                    "[-] Documento inválido. Somente '.docx' ou '.odt'",
                    "são suportados."
                )
                return False

            if (
                self.system == "Windows"
                and self.__document_file.lower().endswith(".docx")
            ):
                docx_convert(self.__document_file, self.__name_file_pdf)
                return True

            return self.convert_with_libreoffice()

        except Exception as e:
            print(f"[-] Erro ao converter para PDF: {e}")
            return False

    def is_valid_document(self) -> bool:
        return (
            self.__document_file.lower().endswith(('.docx', '.odt'))
            and os.path.isfile(self.__document_file)
        )

    def convert_with_libreoffice(self) -> bool:
        try:
            output_dir = os.path.dirname(os.path.abspath(self.__name_file_pdf))
            output_name = os.path.basename(self.__name_file_pdf)

            # Copia o arquivo original com o nome final desejado
            temp_path = os.path.join(output_dir, output_name)
            subprocess.run([
                "libreoffice",
                "--headless",
                "--convert-to", "pdf",
                "--outdir", output_dir,
                self.__document_file
            ], check=True)

            # Renomeia o PDF gerado para o nome desejado (caso precise)
            basename_no_ext = (
                os.path.splitext(os.path.basename(self.__document_file))[0]
            )
            generated_pdf = os.path.join(output_dir, f"{basename_no_ext}.pdf")
            if os.path.exists(generated_pdf) and generated_pdf != temp_path:
                os.rename(generated_pdf, temp_path)

            return True
        except Exception as e:
            print(f"[-] Erro ao usar LibreOffice: {e}")
            return False


if __name__ == "__main__":
    conversor = ConvertDocxToPdf(
        "Portfolio_BethLev_Express.odt",  # ou .docx
        "BethLev_Final.pdf"              # nome final desejado
    )
    conversor.convert_to_pdf()
