from flask import Flask, send_file
from escpos.printer import Usb

app = Flask(__name__)

@app.route('/')
def index():

    # Create a new instance of the printer object
    printer = Usb(0x4b43, 0x3830, 0, 0x81, 0x03) 

    #content to print
    content = 'timestamps nya'
    
    #Mulai Print Text Tiketnya
    # Set align
    printer.set(align='center')
    printer.text('SATPAS POLRES PURWOREJO\n')
    printer.set(align='center')
    printer.text('------------------------\n')
    printer.set(align='center')
        # lewat satu baris
    printer.text('\n')    
    printer.text('lay')
    printer.text('\n')
    printer.set(align='center')
    printer.text('------------------------\n')
    printer.set(align='center')
    printer.text('\n')
    printer.text('ks' 'queue_number')
    printer.text('\n')
    printer.set(align='center')
    #kode QR Code nya
    printer.qr(content, size=16)
    printer.set(align='center')
    printer.text('------------------------\n')
    printer.set(align='center')
    printer.text('Mohon sabar menunggu\n')
    printer.set(align='center')
    printer.text('jam')
    printer.text('\n')
    printer.set(align='center')

    # Cut the paper
    printer.cut()

    return 'Berhasil di print'
    
if __name__ == '__main__':
    app.run(debug=True)


