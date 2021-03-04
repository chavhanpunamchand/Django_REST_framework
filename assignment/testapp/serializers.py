from rest_framework import serializers




class serializer_class:
    try:
        response = {}
        responsedata = []
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            if serializers.validated_data['end_hour'] < serializers.validated_data['start_hour']:
                response["result"] = 0
                response["errors"] = ["Incorrect Timing"]
                self.add_api_call(request, response)
                return Response(response, status=status.HTTP_200_OK)

            plan_range = serializers.validated_data['plan_range']
            days = 1 if plan_range == 'D' else 7 if plan_range == "W" else 31
            start_time = serializers.validated_data['start_hour']
            # end_time = (datetime.datetime.combine(datetime.date.today(), serializers.validated_data['end_time']) - datetime.timedelta(minutes=60)).time()
            end_time = serializers.validated_data['end_hour']

            hours = []
            break_down = 0
            while start_time < end_time:
                data = {"start_hour": start_time.strftime('%H:%M')}
                start_time = (datetime.datetime.combine(datetime.date.today(), start_time) + datetime.timedelta(
                    minutes=serializers.validated_data['interval'])).time()
                data['end_hour'] = start_time.strftime('%H:%M')
                start_time = (datetime.datetime.combine(datetime.date.today(), start_time) + datetime.timedelta(
                    minutes=serializers.validated_data['gap'])).time()  # gap period
                if start_time > end_time:
                    pass
                else:
                    hours.append(data)

                if break_down > 500:
                    response['result'] = 1
                    response['data'] = ['Infinite Loop Detected']
                    self.add_api_call(request, response)
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    break_down = break_down + 1

            days_list = []

            for i in hours:
                day_obj = {}

                for j in range(days):
                    day_obj[j] = i

                days_list.append(day_obj)

            # [days_list.append({i:hours}) for i in range(days)]

            response['result'] = 1
            response['data'] = days_list
            self.add_api_call(request, response)
            return Response(response, status=status.HTTP_200_OK)
        else:
            response['result'] = 0
            response = handle_errors(serializers.errors)
            self.add_api_call(request, response)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        response["result"] = 0
        responsedata.append(str(e))
        response['errors'] = responsedata
        self.add_api_call(request, response)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
