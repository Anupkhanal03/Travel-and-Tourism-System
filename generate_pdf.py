import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO

def generate_ticket_pdf(booking_data):
    """
    Generates a PDF ticket in memory and returns a BytesIO object.
    booking_data should be a dict with: full_name, email, package_title, travel_date, num_people, total_price, transaction_id, etc.
    """
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    p.setFont("Helvetica-Bold", 24)
    p.drawString(50, height - 80, "Smart Nepal Travel System")
    
    p.setFont("Helvetica", 14)
    p.drawString(50, height - 110, "Booking Confirmation Ticket")
    
    # Divider
    p.line(50, height - 120, width - 50, height - 120)
    
    # Booking Details
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, height - 160, "Customer Information:")
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 180, f"Name: {booking_data.get('full_name', '')}")
    p.drawString(50, height - 200, f"Email: {booking_data.get('email', '')}")
    
    p.setFont("Helvetica-Bold", 12)
    p.drawString(300, height - 160, "Trip Details:")
    p.setFont("Helvetica", 12)
    p.drawString(300, height - 180, f"Package: {booking_data.get('package_title', '')}")
    p.drawString(300, height - 200, f"Travel Date: {booking_data.get('travel_date', '')}")
    p.drawString(300, height - 220, f"Number of People: {booking_data.get('num_people', '')}")
    
    # Divider
    p.line(50, height - 250, width - 50, height - 250)
    
    # Payment Details
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, height - 290, "Payment Summary:")
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 310, f"Total Price: Rs. {booking_data.get('total_price', 0)}")
    p.drawString(50, height - 330, f"Payment Status: {booking_data.get('payment_status', 'Pending')}")
    if booking_data.get('transaction_id'):
        p.drawString(50, height - 350, f"Transaction ID: {booking_data.get('transaction_id')}")
        
    # Footer message
    p.setFont("Helvetica-Oblique", 10)
    p.drawString(50, 50, "Thank you for choosing Smart Nepal Travel System. Have a great trip!")
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer
