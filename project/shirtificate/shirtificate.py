""" LAST EXERCISE BEFORE BIG FINALE <3 HEHEH LETS GOOO! """

from fpdf import FPDF


def main():
    user = input("What's your name? ")
    shirt_factory(user + ' took CS50')


def shirt_factory(stamp):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=35, y=80,w=140,h=200)
    pdf.set_font('helvetica', 'B', 18)
    pdf.set_xy(6, 105)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(200,50,stamp,fill=False, align='C')
    pdf.set_font('helvetica', 'B', 28)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(6, 20)
    pdf.cell(200,80,'CS50 Shirtificate',fill=False, align='C')
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()

