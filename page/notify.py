from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import RequestContext
from django.conf import settings
# from email.MIMEImage import MIMEImage


class Notify():

    def __init__(self, *args, **kwargs):
        self.template = kwargs["template"]
        self.subject = kwargs["subject"]
        self.receiver = kwargs["receiver"]
        self.data = kwargs["data"]
        self.request = kwargs.get("request", None)
        self.sender = kwargs.get("sender", settings.EMAIL_SENDER_ADDRESS)
        self.kwargs = kwargs
        self.set_context()
        self.set_text()
        self.set_html()

    def set_context(self):
        if self.request:
            self.context = RequestContext(self.request, self.data)
        else:
            self.context = self.data

    def set_text(self):
        self.text = render_to_string(
            u"{}.txt".format(self.template),
            self.context
        )

    def set_html(self):
        self.html = render_to_string(
            u"{}.html".format(self.template),
            self.context
        )

    def set_attachments(self, msg):
        if "attachments" in self.kwargs:
            for attach in self.kwargs["attachments"]:
                msg.attach_file(attach)
        return msg

    def set_stream_attachments(self, msg):
        if "stream_attachments" in self.kwargs:
            for attach in self.kwargs["stream_attachments"]:
                msg.attach(
                    attach.name, attach.file.read(), attach.content_type
                )
        return msg

    # def set_embedded_images(self, msg):
    #     if "images" in self.kwargs:
    #         for img in self.kwargs["images"]:
    #             self.email_embed_image(msg, img.name, img.read())
    #     return msg

    # def email_embed_image(msg, img_content_id, img_data):
    #     img = MIMEImage(img_data)
    #     img.add_header('Content-ID', '<%s>' % img_content_id)
    #     img.add_header('Content-Disposition', 'inline')
    #     msg.attach(img)

    def send(self):
        try:
            print = "Sending from: ", self.sender
            print = "Sending to: ", self.receiver

            msg = EmailMultiAlternatives(
                self.subject,
                self.text,
                self.sender,
                [self.receiver, ],
            )

            self.set_attachments(msg)
            self.set_stream_attachments(msg)

            if len(self.html):
                msg.attach_alternative(self.html, "text/html")
            return msg.send()
        except Exception as e:
            print = "ECCEZIONE ", e