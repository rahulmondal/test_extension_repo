# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Globex Corporation
# All rights reserved.
#
from connect.eaas.core.decorators import (
    event,
    variables,
)
from connect.eaas.core.extension import EventsApplicationBase
from connect.eaas.core.responses import (
    BackgroundResponse,
)


@variables([
    {
        'name': 'VAR_NAME_1',
        'initial_value': 'VAR_VALUE_1',
        'secure': False,
    },
    {
        'name': 'VAR_NAME_N',
        'initial_value': 'VAR_VALUE_N',
        'secure': True,
    },
])
class MyAwesomeProjectEventsApplication(EventsApplicationBase):
    @event(
        'asset_change_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_change_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_resume_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_resume_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_purchase_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_purchase_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_suspend_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_suspend_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()
