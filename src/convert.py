import os
import textract

OCR = ['.pdf', '.png', '.jpeg', '.jpg']

class FileConverter:
    def convert(self, file: str, file_extension: str, encoding: str = 'utf-8') -> str:
        _text = ""

        attempts = 1
        ocr = True
        while attempts >= 0:
            try:
                if file_extension in OCR:
                    _text = textract.process(file, method='tesseract', language='rus').decode(encoding)
                else:
                    _text = textract.process(file).decode(encoding)
                break
            except Exception as e:
                print('Conversion issue:', file, e)
                print(f"Conversion issue: {str(e)}\n")

                if file_extension in OCR:
                    ocr = not ocr
                    attempts -= 1

                if "Rich Text" in str(e):
                    os.rename(file, file + '.rtf')
                    file = file + '.rtf'
                    attempts -= 1
                else:
                    raise e

        return _text

if __name__ == '__main__':
    # print(FileConverter().convert('../d.pdf', '.pdf'))
    print(FileConverter().convert('../kk/m.pdf', '.pdf'))