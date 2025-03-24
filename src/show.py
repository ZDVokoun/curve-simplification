import matplotlib.pyplot as plt
import metrics

# Funkce pro vykreslení bodů a jejich spojení
def vykresli_body(body, nove_body, cyklus, file = None):
    # Rozdělení bodů na souřadnice x a y
    if cyklus:
        body.append(body[0])
    x = [bod[0] for bod in body]
    y = [bod[1] for bod in body]

    # Vykreslení bodů
    plt.scatter(x, y, color='red')

    # Spojení bodů
    plt.plot(x, y, color='red')

    x = [bod[0] for bod in nove_body]
    y = [bod[1] for bod in nove_body]

    # Vykreslení bodů
    plt.scatter(x, y, color='blue')

    # Spojení bodů
    plt.plot(x, y, color='blue')

    # Přidání názvu os a zobrazení grafu
    plt.xlabel('X souřadnice')
    plt.ylabel('Y souřadnice')
    plt.title('Bodová grafika a spojnice')
    plt.grid(True)

    if file:
        plt.savefig(file + " - " + str(metrics.MSE(body,nove_body)) + ".pdf")

    plt.show()

