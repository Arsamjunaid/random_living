from odoo import http
from odoo.http import request
import json

class StudentWebhookController(http.Controller):
    # @http.route('/webhook/student', type='json', auth='public', methods=['POST'], csrf=False)
    # def create_or_update_student(self):
    #     data = request.jsonrequest
    #
    #     email = data.get('email')
    #     username = data.get('username')
    #     password = data.get('password')
    #     course_id = data.get('course_id')
    #
    #     if not email or not username or not password or not course_id:
    #         return {'status': 'error', 'message': 'Missing required fields'}
    #
    #     # Check if the student already exists
    #     student = request.env['student.student'].sudo().search([('email', '=', email)], limit=1)
    #
    #     if student:
    #         # Activate the course for the existing student
    #         course = request.env['course.course'].sudo().browse(course_id)
    #         if course:
    #             student.write({'course_ids': [(4, course_id)]})
    #             return {'status': 'success', 'message': 'Course activated for existing student'}
    #         else:
    #             return {'status': 'error', 'message': 'Course not found'}
    #     else:
    #         # Create a new student
    #         student = request.env['student.student'].sudo().create({
    #             'email': email,
    #             'username': username,
    #             'password': password,
    #             'course_ids': [(4, course_id)]
    #         })
    #         return {'status': 'success', 'message': 'New student created and course activated'}
    #
    #     return {'status': 'error', 'message': 'An error occurred'}


    @http.route('/webhook/receive', type='json', auth='public', methods=['POST'], csrf=False)
    def receive_webhook(self, **kwargs):
        # Extract data from the request
        email = kwargs.get('email')
        username = kwargs.get('username')
        course_id = kwargs.get('course_id')
        password = kwargs.get('password')

        # Process the data (for example, log it or save it to the database)
        request.env['my.webhook.log'].sudo().create({
            'email': email,
            'username': username,
            'course_id': course_id,
            'password': password
        })

        return {'status': 'success', 'message': 'Data received successfully'}

    # if not email or not username or not password or not course_id:
    #     return {'status': 'error', 'message': 'Missing required fields'}
    #
    #     # Check if the student already exists
    # student = request.env['my.webhook'].sudo().search([('email', '=', email)], limit=1)
    #
    # if student:
    #     # Activate the course for the existing student
    #     course = request.env['course.course'].sudo().browse(course_id)
    #     if course:
    #         student.write({'course_ids': [(4, course_id)]})
    #         return {'status': 'success', 'message': 'Course activated for existing student'}
    #     else:
    #         return {'status': 'error', 'message': 'Course not found'}
    # else:
    #     # Create a new student
    #     student = request.env['my.webhook'].sudo().create({
    #         'email': email,
    #         'username': username,
    #         'password': password,
    #         'course_ids': [(4, course_id)]
    #     })
    #     return {'status': 'success', 'message': 'New student created and course activated'}
    #
    # return {'status': 'error', 'message': 'An error occurred'}
    #     # Extract data from the request
    #     email = kwargs.get('email')
    #     username = kwargs.get('username')
    #     course_id = kwargs.get('course_id')
    #     password = kwargs.get('password')
    #     option = kwargs.get('option', 'default')
    #
    #     # Process the data based on the option
    #     if option == 'log':
    #         # Log the data to the database
    #         request.env['my.webhook.log'].sudo().create({
    #             'email': email,
    #             'username': username,
    #             'course_id': course_id,
    #             'password': password
    #         })
    #         return {'status': 'success', 'message': 'Data logged successfully'}
    #
    #     elif option == 'notify':
    #         # Send a notification (this is just an example, implement your notification logic here)
    #         # For example, you can use an Odoo email template to send an email
    #         template_id = request.env.ref('your_module.email_template_webhook_notification').id
    #         request.env['mail.template'].browse(template_id).send_mail(1, force_send=True, email_values={'email_to': email})
    #         return {'status': 'success', 'message': 'Notification sent successfully'}
    #
    #     else:
    #         return {'status': 'error', 'message': 'Invalid option'}
    #
    #     self._save_to_marketing_system(email, username, course_id)
    #
    #     request.env['student.student'].sudo().create({
    #         'email': email,
    #         'name': username,
    #         'course_id': course_id,
    #         'password': password,
    #     })
    #
    #     return {'status': 'success'}
    #
    # def _save_to_marketing_system(self, email, username, course_id):
    #     # Implement your logic to save data to the marketing system
    #     pass
