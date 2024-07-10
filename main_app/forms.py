from django import forms

class AircraftTypeForm(forms.Form):
    name = forms.CharField(max_length=250)
    active = forms.BooleanField(required=False, initial=False)
    

class ServiceLoadForm(forms.Form):
    serviceload_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    service_load_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    service_qty = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    max_children = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    max_infants = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    seat_map = forms.ChoiceField(
        choices=[('', '---select---')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    iata_identifier = forms.ChoiceField(
        choices=[('', '---select---')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class AirCraftForm(forms.Form):
    aircraft_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_registration = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_capacity = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_type = forms.ChoiceField(
        choices=[('', 'Select Aircraft Type')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    seatmap = forms.ChoiceField(
        choices=[('', 'Select Seat Map')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    max_cargo_weight = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    calendar_color = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class SaveRouteForm(forms.Form):
    saveroute_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fromdate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    todate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    miles = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    hours = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    aircraft_type = forms.ChoiceField(
        choices=[('', 'Select Aircraft Type')]  ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class DSTNotificationsForm(forms.Form):
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    dstnotification_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    aircraft_id = forms.ChoiceField(
        choices=[('', 'Select Aircraft')] ,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    destination = forms.ChoiceField(
        choices=[('', 'Select Destination')] ,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    service_from = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    service_to = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    showon = forms.ChoiceField(
        
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    notification = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    color = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    font_size = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'})
    )
    bold = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    user_availability_screen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    agents_crs_availability_screen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    PNR_screen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    ref_template = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    show_on_seatcontrol = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )

class DSTRestrictForm(forms.Form):
    destination= forms.ChoiceField(
        choices=[('', 'Select Destination')] ,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    dstrestrict_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    fromdate = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    todate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    flight_number = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    notification = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )

class DSTTimeAddonForm(forms.Form):
    dstaddon_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    destination_id = forms.ChoiceField(
        choices=[('', 'Select Destination')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    flight_number = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    time_add = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fromdate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    todate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    add_to = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class AcAvailabilityForm(forms.Form):
    name = forms.CharField(max_length=250)
    active = forms.BooleanField(required=False, initial=False)
    
    ac_number = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    type = forms.ChoiceField(
        choices=[('', 'Select Type')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date_from = forms.DateField( label="From",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    date_to = forms.DateField( label="To",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    status = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class AcAvailabilityTypeForm(forms.Form):
    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    color = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )

class SpecialServicesForm(forms.Form):
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    ss_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_id = forms.ChoiceField(
        choices=[('', 'Select Aircraft')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    block_online_checkin = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    add_to_assistance_list = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    block_ssr_for_mmb = forms.BooleanField( label="Block SSR for MMB",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    show_on_web = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    order = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    code = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    max_per_flight = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    detailed_description = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class QueuesForm(forms.Form):
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    queue_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    webhook = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input' , 'style': 'margin-left: 10px;'})
    )
    queue_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    queue_type = forms.ChoiceField(
      
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    unq = forms.CharField( label="UNQ",
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    agt_id = forms.CharField( label="AGT id",
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    webhook_url = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )



class DestinationForm(forms.Form):
    order = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    show = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    destination_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_id = forms.ChoiceField(
        choices=[('', 'Select Aircraft')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    father = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_on_web = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    charge_tax_on_infant = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    block_from_pre_book = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    code = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    time_zone = forms.ChoiceField(
        choices=[('', 'Select Time Zone')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    lat = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    long = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    father_code = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    allow_strip_change = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    father_destination = forms.ChoiceField(
        choices=[('', 'Select Father Destination')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    crs_color = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    accommodation_mandatory = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    crs_show = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    crs_order = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    baggage_allowance = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    checkin_time_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    online_checkin_open_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    block_online_seat_selection = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    online_checkin_close_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    min_booking_interval_hr = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    min_passenger = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    boarding_time_minutes = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    bar_code_version = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    web_min_booking_interval_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    gate_closing_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    baggage_drop_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    airport_control_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    pnl_timing = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    adl_timing = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    adl_continuous = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pal_timing = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    send_crew_msg = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    use_icao_code_with_flight_number = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    send_pal_cal = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    sita_address_es = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    http_address_es = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    pal_cal_sita_address_es = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    pal_cal_e_mail_s = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    movementtract_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    template = forms.ChoiceField(
       
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sightseeing = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    return_destination = forms.ChoiceField(
        choices=[('', 'Select Return Destination')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class ReftemplateForm(forms.Form):
    service_choices = [
        ('All_service', 'All service'),
        ('Flights_and_Open_Service', 'Flights and Open Service'),
        ('Flights_Only', 'Flights Only'),
        ('Flights, Charters and Open Service', 'Flights, Charters and Open Service'),
        ('Flights, Charters, Open Service and Ancillaries', 'Flights, Charters, Open Service and Ancillaries'),
        ('Flights, Products and Hotels', 'Flights, Products and Hotels'),
    ]
    
    name = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={"class": "form-control "}))
    language = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    title_e_mail_subject = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    show_services = forms.ChoiceField(choices=service_choices, required=True, widget=forms.Select(attrs={"class": "form-control"}))
    active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    show_on_agents_crs = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    show_only_to_ticketed_pnr = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    show_to_agent_pnr = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    show_to_direct_cust_pnr = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    agent_logo = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    customer_agent_details = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    company_logo = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    company_details = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    qr_code = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    personal_tickets = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control form-control-sm"}))
    intro_text = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
    title_note = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    services_with_pricing = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    services_without_pricing = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    total = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    fare_basis = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    vat = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    company_currency = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    class_code = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    class_name = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    currency_name = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    check_in_status = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    exchange_rate = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    checkin_hhmm = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    gds_rloc_instead_of_pnr = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    show_rack = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    baggage = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    checkin = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    pnr_remarks = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    website_link = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    passengers = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    flight_rules_and_notifications = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    tax_breakdown = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    fare_breakdown = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    show_ptl = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    pnr_name = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    show_via = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    ssr = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    show_due = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    pnr_log = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    show_ttl = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    receipts = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    invoices = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    deposits = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    vouchers_info = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    ticket_terms = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    environment = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    e_ticket = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    accommodations = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    terminals = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    full_pax_details = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    seats = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    cabin_class = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    short_pnr = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    show_etkt = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    hide_timings_for_non_flights = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    cargo_tracking_code = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    gate_closing = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    baggage_drop = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    footer_text = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
    attachment_1 = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    attachment_2 = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))




class ReftlangmasterForm(forms.Form):
    active = forms.BooleanField(initial=False, required=False)
    language_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    language_code = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))



class TermsAndConditionsForm(forms.Form):
    individual = forms.BooleanField(
        label='Individual',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input','style': 'margin-left: 10px;'})
    )
    active = forms.BooleanField(
        label='Active',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input','style': 'margin-left: 10px;'})
    )
    default = forms.BooleanField(
        label='Default',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input','style': 'margin-left: 10px;'})
    )
    language = forms.CharField(
        label='Language',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    term_and_condition_text = forms.CharField(
        label='Term and Condition Text',
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 4}),
        required=False
    )


class ManifestTemplateForm(forms.Form):
    active = forms.BooleanField(
        label='Active',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    name = forms.CharField(
        label='Name *',  # Add asterisk to label
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'required': 'required'})
    )
    code = forms.CharField(
        label='Code *',  # Add asterisk to label
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'required': 'required'})
    )
    header_subject = forms.CharField(
        label='Header/Subject *',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'required': 'required'})
    )
    filter_with_check_in_status = forms.CharField(
        label='Filter with Check-In Status ',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    show_only_ticketed = forms.BooleanField(
        label='Show Only Ticketed *',
        initial=False,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': 'required'})
    )
    group_by = forms.CharField(
        label='Group By *',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'required': 'required'})
    )
    filter_with_service_status = forms.CharField(
        label='Filter with Service Status *',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'required': 'required'})
    )
    sub_header = forms.CharField(
        label='Sub Header',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )


class PrintOutDetailsManifestForm(forms.Form):
    manifest = forms.ChoiceField(
        label='Manifest',
        choices=[],  # Populate this with the appropriate choices
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    num = forms.BooleanField(
        label='Num',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    user_class = forms.BooleanField(
        label='User Class',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    check_in_status = forms.BooleanField(
        label='Check-in Status',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    seat = forms.BooleanField(
        label='Seat',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    date_of_birth = forms.BooleanField(
        label='Date of Birth',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    gender = forms.BooleanField(
        label='Gender',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    class_allowance = forms.BooleanField(
        label='Class Allowance',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    passport_issue_country = forms.BooleanField(
        label='Passport Issue Country',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pax_weight = forms.BooleanField(
        label='Pax Weight',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    trip_type = forms.BooleanField(
        label='Trip Type',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    boarding_tag_color = forms.BooleanField(
        label='Boarding Tag Color',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pax_name = forms.BooleanField(
        label='Pax Name',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    a_c = forms.BooleanField(
        label='A/C',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    title = forms.BooleanField(
        label='Title',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    e_mail = forms.BooleanField(
        label='E-mail',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    cargo_weight = forms.BooleanField(
        label='Cargo Weight',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_document_code = forms.BooleanField(
        label='Show Document Code',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_ancillary_services = forms.BooleanField(
        label='Show Ancillary Services',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    breakdown_block = forms.BooleanField(
        label='Breakdown Block',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    passenger_remark = forms.BooleanField(
        label='Passenger Remark',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    baggage_tag = forms.BooleanField(
        label='Baggage Tag',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pnr_ref = forms.BooleanField(
        label='PNR Ref',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    splitfirstlast = forms.BooleanField(
        label='Split First/Last',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    tkt_ref = forms.BooleanField(
        label='TKT Ref',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    nop = forms.BooleanField(
        label='NOP',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    passport_expiry = forms.BooleanField(
        label='Passport Expiry',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    breakrows = forms.BooleanField(
        label='Break Rows',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_ancillary_summary = forms.BooleanField(
        label='Show Ancillary Summary',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_check_in_summary = forms.BooleanField(
        label='Show Check-in Summary',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_coupons = forms.BooleanField(
        label='Show Coupons',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    bgg_weight = forms.BooleanField(
        label='BGG Weight',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pnr_status = forms.BooleanField(
        label='PNR Status',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    b_pass = forms.BooleanField(
        label='B Pass',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pay_ci = forms.BooleanField(
        label='Pay CI',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    origin = forms.BooleanField(
        label='Origin',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    doc_number = forms.BooleanField(
        label='Doc Number',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_ssr_totals = forms.BooleanField(
        label='Show SSR Totals',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_ssr_remarks = forms.BooleanField(
        label='Show SSR Remarks',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_ssr = forms.BooleanField(
        label='Show SSR',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    phone = forms.BooleanField(
        label='Phone',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    place_of_birth = forms.BooleanField(
        label='Place of Birth',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    yyyymmdd_dates = forms.BooleanField(
        label='YYYYMMDD Dates',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_pnr_user_name_in_origin = forms.BooleanField(
        label='Show PNR User Name in Origin',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    nationality = forms.BooleanField(
        label='Nationality',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pnr_remarks = forms.BooleanField(
        label='PNR Remarks',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    crew_on_top = forms.BooleanField(
        label='Crew on Top',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pax_body_temp = forms.BooleanField(
        label='Pax Body Temp',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    fare_basis = forms.BooleanField(
        label='Fare Basis',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    cow_weight = forms.BooleanField(
        label='Cow Weight',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    cow_nop = forms.BooleanField(
        label='Cow NOP',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class PrintOutBottomManifestForm(forms.Form):
    manifest = forms.ChoiceField(
        label='Manifest',
        choices=[],  # Populate this with the appropriate choices
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    pax_total = forms.BooleanField(
        label='Pax Total',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pax_picks = forms.BooleanField(
        label='Pax Picks',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pax_drops = forms.BooleanField(
        label='Pax Drops',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    nop_total = forms.BooleanField(
        label='NOP Total',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    bgg_weight_total = forms.BooleanField(
        label='BGG Weight Total',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pax_weight_total = forms.BooleanField(
        label='Pax Weight Total',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pnr_on_rq = forms.BooleanField(
        label='PNR on RQ',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    selected_crew = forms.BooleanField(
        label='Selected Crew',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    cargo_list = forms.BooleanField(
        label='Cargo List',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    always_show_cargo = forms.BooleanField(
        label='Always Show Cargo',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    remarks = forms.BooleanField(
        label='Remarks',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    text_crew = forms.BooleanField(
        label='Text Crew',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    fuel = forms.BooleanField(
        label='Fuel',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    routing = forms.BooleanField(
        label='Routing',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    cow_weight = forms.BooleanField(
        label='Cow Weight',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    cow_nop = forms.BooleanField(
        label='Cow NOP',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    signature = forms.BooleanField(
        label='Signature',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    footer_text = forms.CharField(
        label='Footer Text',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'})
    )

class BookingpurposeForm(forms.Form):
    active = forms.BooleanField(
        label='Active',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: px;'})
    )
    name = forms.CharField(
        label='Name',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )



class ServicessuppliersForm(forms.Form):
    active = forms.BooleanField(
        label='Active',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input','style': 'margin-left: px;'})
    )
    supplier_name = forms.CharField(
        label='Supplier Name',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )

class ServicestypesForm(forms.Form):
    active = forms.BooleanField(
        label='Active',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    type_name = forms.CharField(
        label='Type Name',
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    income_code = forms.CharField(
        label='Income Code',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    service_template = forms.CharField(
        label='Service Template',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'})
    )



class Reftwords(forms.Form):
    
    translated = forms.CharField(
        label='Translated',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
   
    default_language = forms.ChoiceField(
        label='Default(English)',
        choices=[('english', 'English')],  # Add more languages as needed
        initial='english',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
   
    language = forms.CharField(
        label='Language',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )

class ScheduledreportsForm(forms.Form):
    active = forms.BooleanField(
        label='Active',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    user = forms.CharField(
        label='User',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    report = forms.CharField(
        label='Report',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    time_of_day = forms.ChoiceField(
        label='Time of Day',
        choices=[
            ('morning', 'Morning'),
            ('afternoon', 'Afternoon'),
            ('evening', 'Evening'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    frequency = forms.ChoiceField(
        label='Frequency',
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    timing = forms.CharField(
        label='Timing',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
   
    email = forms.EmailField(
        label='Email To',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    sendto = forms.EmailField(
        label='Send To',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )



class StationvatForm(forms.Form):
    active = forms.BooleanField(
        label='Active',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    vat = forms.CharField(
        label='VAT',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    origin = forms.CharField(
        label='Origin',
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    station_name = forms.CharField(
        label='Station Name',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class SmstemplateForm(forms.Form):
    LANGUAGE_CHOICES = (
    ('open', 'Open'),
    # Add other language choices as needed
)

    active = forms.BooleanField(
        label='Active',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    send_sms_on_ff_spend = forms.BooleanField(
        label='Send SMS on FF Spend',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    send_sms_on_ff_earn = forms.BooleanField(
        label='Send SMS on FF Earn',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    name = forms.CharField(
        label='Name',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Message',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    language = forms.ChoiceField(
        label='Language',
        choices=LANGUAGE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
   
class UsergroupmasterForm(forms.Form):
    active = forms.BooleanField(
        label='Active',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    permission_type_id = forms.ChoiceField(
        label='Permission Type',
        choices=[(1, 'Type 1'), (2, 'Type 2')],  # Replace with actual choices
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    group_name = forms.CharField(
        label='Group Name',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class ReportsupermissionsForm(forms.Form):
    REPORT_CHOICES = [
        ('report1', 'Report 1'),
        ('report2', 'Report 2'),
        ('report3', 'Report 3'),
    ]

    USER_CHOICES = [
        ('user1', 'User 1'),
        ('user2', 'User 2'),
        ('user3', 'User 3'),
    ]

    report = forms.ChoiceField(
        label='Report',
        choices=REPORT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    user = forms.ChoiceField(
        label='User',
        choices=USER_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
