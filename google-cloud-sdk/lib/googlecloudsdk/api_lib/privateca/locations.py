# Lint as: python3
# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Helpers for dealing with Private CA locations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.privateca import base
from googlecloudsdk.core import properties


def GetSupportedLocations():
  """Gets a list of supported Private CA locations for the current project."""
  client = base.GetClientInstance()
  messages = base.GetMessagesModule()

  project = properties.VALUES.core.project.GetOrFail()

  response = client.projects_locations.List(
      messages.PrivatecaProjectsLocationsListRequest(
          name='projects/{}'.format(project)))
  return map(lambda location: location.locationId, response.locations)
