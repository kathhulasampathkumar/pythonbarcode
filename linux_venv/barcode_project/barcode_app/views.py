from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.http import JsonResponse

from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt 

from zebra import Zebra
import logging

# Create your views here.
def index(request):
    try:
        # Initialize the Zebra printer
        z = Zebra()

        # Specify the name of your Zebra printer (check your printer name)
        z.setqueue("Your_Zebra_Printer_Queue_Name")

        # Create the ZPL (Zebra Programming Language) string for the barcode
        barcode_data = "^XA^FO50,50^BCN,100,Y,N,N^FD1234567890^FS^XZ"

        # Send the ZPL string to the printer
        z.output(barcode_data)

        return HttpResponse("Barcode sent to the printer.")
    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        return HttpResponse(f"Error: {e}", status=500)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return HttpResponse(f"Unexpected error: {e}", status=500)
