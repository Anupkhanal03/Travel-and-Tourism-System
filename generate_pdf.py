import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_ticket_pdf(booking):
    """
    Generates a PDF ticket for a booking.
    Returns a BytesIO buffer containing the PDF data.
    """
    buffer = io.BytesIO()
    
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Title
    p.setFont("Helvetica-Bold", 24)
    p.setFillColor(colors.darkblue)
    p.drawString(200, height - 50, "Nepal Travel System")
    
    p.setFont("Helvetica-Bold", 18)
    p.setFillColor(colors.black)
    p.drawString(250, height - 80, "Booking Ticket")
    
    # Line
    p.line(50, height - 100, width - 50, height - 100)
    
    # Booking details
    p.setFont("Helvetica", 12)
    y_position = height - 130
    
    details = [
        f"Booking ID: {booking.get('id', 'N/A')}",
        f"Name: {booking.get('full_name', 'N/A')}",
        f"Email: {booking.get('email', 'N/A')}",
        f"Package: {booking.get('package_title', 'N/A')}",
        f"Number of People: {booking.get('num_people', 'N/A')}",
        f"Travel Date: {booking.get('travel_date', 'N/A')}",
        f"Total Price: Rs. {booking.get('total_price', '0.00')}",
        f"Payment Status: {booking.get('payment_status', 'N/A')}",
        f"Transaction ID: {booking.get('transaction_id', 'N/A')}"
    ]
    
    for detail in details:
        p.drawString(100, y_position, detail)
        y_position -= 30
        
    # Footer
    p.setFont("Helvetica-Oblique", 10)
    p.drawString(50, 50, "Thank you for choosing Nepal Travel System! Have a safe trip.")
    
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer
