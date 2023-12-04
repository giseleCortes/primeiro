from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = navegador.new_page()
    pagina.goto('https://microstrategy.itapevarec.com.br/MicroStrategy/asp/Main.aspx')
    pagina.fill('xpath=//*[@id="Uid"]', '**************')
    pagina.fill('//*[@id="Pwd"]', '*************')
    pagina.locator('xpath=//*[@id="3054"]').click()
    pagina.locator('xpath=//*[@id="projects_ProjectsStyle"]/table/tbody/tr/td[1]/div/table/tbody/tr/td[2]/a').click()
    pagina.locator('xpath=//*[@id="dktpSectionView"]/a[3]/div[3]').click()
    pagina.locator('xpath=//*[@id="ncsList4096"]/tbody/tr[11]/td[2]').click()
    pagina.locator('xpath=//*[@id="ribbonToolbarTabsListContainer"]/div[1]/table/tbody/tr/td[3]').click()
    pagina.locator('xpath=//*[@id="RptHomeMenu_"]/tbody/tr/td/div/div[18]/a/div[2]').click()
    pagina.locator('xpath=//*[@id="RptHomeExportMenu_WEB-INFxmllayoutsblocksHomeExportMenuLayoutxml"]/tbody/tr/td/div/div[4]/a').click()

    #pagina da erro por abre uma segunda pagina como o mesmo titulo da Primeira 