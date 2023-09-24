import smtplib

my_email = "dummy@mail.com"
password ="1234567"

with smtplib.SMTP("smtp.mail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="dummy2@mail.com",
        msg="Subject:Hello World! \n\n This is the body of my email."
    )
