class ErrorsMessages:
    field_required = {'status': 'PS-0091', 'message': 'The field is required'}
    field_is_blank = {'status': 'PS-0092', 'message': 'The field can`t be blank'}
    register_failed = {'status': 'PS-0001', 'message': 'Error during user registration'}
    min_length = {'status': 'PS-0002', 'message': 'please your password must be min 8 characters'}
    max_length = {'status': 'PS-0003', 'message': "please your password must be max 16 characters"}
    user_name_min = {'status': 'PS-0004', 'message': 'please your user name must be min 8 characters'}
    user_name_max = {'status': 'PS-0005', 'message': 'please your user name must be max 25 characters'}
    document_id_format = {'status': 'PS-0006', 'message': 'please check the format of your document id'}
    password_bad_format = {'status': 'PS-0007', 'message': 'please check the format of your password'}
    mobile_number_format = {'status': 'PS-0008', 'message': 'please check the format of your mobile number'}
    email_format = {'status': 'PS-0009', 'message': 'please check the format of your email'}
    method_not_allowed = dict({'status': 'PS-9010', 'message': 'Method not allowed'})

