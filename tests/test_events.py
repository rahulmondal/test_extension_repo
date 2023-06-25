# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Globex Corporation
# All rights reserved.
#
from connect_ext.events import MyAwesomeProjectEventsApplication


def test_handle_asset_change_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = MyAwesomeProjectEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_change_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_resume_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = MyAwesomeProjectEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_resume_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_purchase_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = MyAwesomeProjectEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_purchase_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_suspend_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = MyAwesomeProjectEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_suspend_request_processing(request)
    assert result.status == 'success'
