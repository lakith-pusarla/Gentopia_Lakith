import io
import requests
from PyPDF2 import PdfReader
from typing import AnyStr
from gentopia.tools.basetool import *


class PDFScanArgs(BaseModel):
    url: str = Field(..., description="PDF URL")
    
class PDFScan(BaseTool):
    

    name = "pdf_scan"
    description = ("Tool to fetch pdf from given URL and read the pdf")

    args_schema: Optional[Type[BaseModel]] = PDFScanArgs

    def _run(self, url: AnyStr) -> str:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}

        response = requests.get(url=url, headers=headers, timeout=120)
        mem_obj = io.BytesIO(response.content)
        pdf_file = PdfReader(mem_obj)

        pdf_obj = pdf_file.pages[0]
        return pdf_obj.extract_text()
         
        
    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = PDFScan()._run("https://arxiv.org/pdf/1706.03762.pdf")
    print(ans)


