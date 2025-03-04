import json
import prompty
import prompty.openai
from pathlib import Path
folder = Path(__file__).parent.absolute().as_posix()

from promptflow.core import tool, Prompty

@tool
def write(    
      productContext: any,
      products: any,
      assignment: any
) -> str:
  # path to prompty (requires absolute path for deployment)
  path_to_prompty = folder + "/writer_llamaLocal.prompty"

  # load prompty as a flow
  flow = Prompty.load(path_to_prompty)
 
  # execute the flow as function
  result = flow(
    productContext = productContext,
    products = products,
    assignment = assignment
  )

  return result

if __name__ == "__main__":
   base = Path(__file__).parent
   products = json.loads(Path(base.parent / "json_files/find_products_output.json").read_text())
   productContext= "Tell me something about mobile phones"
   assignment= "Tell me something about mobile phones"
  # Esecuzione della funzione write
   result = write(productContext, products, assignment)

    # Stampa il risultato generato
   print(result) # Stampa risultato su console

