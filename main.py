from playwright.sync_api import sync_playwright
import time

def encontrar_elemento_na_pagina(page):
    try:
        elemento = page.locator('xpath=//*[@id="3131"]')
        if elemento.is_enabled():
            return elemento
    except:
        pass
    return None

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = navegador.new_page()
    pagina.goto("https://microstrategy.itapevarec.com.br/MicroStrategy/asp/Main.aspx?evt=3001&src=Main.aspx.3001&Port=0&")
    pagina.fill('xpath=//*[@id="Uid"]','wpoliveira')
    pagina.fill('//*[@id="Pwd"]','ibnavi@327134094AASETw!cR0')
    pagina.locator('xpath=//*[@id="3054"]').click()
    pagina.locator('xpath=//*[@id="projects_ProjectsStyle"]/table/tbody/tr/td[1]/div/table/tbody/tr/td[2]/a').click()
    pagina.locator('xpath=//*[@id="dktpSectionView"]/a[3]/div[3]').click()
    pagina.locator('xpath=//*[@id="ncsList4096"]/tbody/tr[11]/td[2]').click()
    pagina.locator('xpath=//*[@id="ribbonToolbarTabsListContainer"]/div[1]/table/tbody/tr/td[3]').click()
    pagina.locator('xpath=//*[@id="RptHomeMenu_"]/tbody/tr/td/div/div[18]/a/div[2]').click()
    pagina.locator('xpath=//*[@id="RptHomeExportMenu_WEB-INFxmllayoutsblocksHomeExportMenuLayoutxml"]/tbody/tr/td/div/div[4]/a').click()

    # Aguardar carregamento da nova página
    pagina.wait_for_load_state('load', timeout=5000)
    
    nova_pagina = None
    for page in contexto.pages:
        if "Opções de exportação. MicroStrategy" in page.title():
            nova_pagina = page
            break

    if nova_pagina:
        print(f"Número de páginas: {len(contexto.pages)}")
        print(f"Página atual: {nova_pagina.url()}")
        
        # Continuar interações com a nova página
        elemento_na_nova_pagina = encontrar_elemento_na_pagina(nova_pagina)
        if elemento_na_nova_pagina:
            elemento_na_nova_pagina.click()
        else:
            print("Elemento não encontrado na nova página.")

    else:
        print("Não foi possível identificar a nova página pelo título.")

    # Aguardar um pouco antes de encerrar o navegador
    time.sleep(5)
    