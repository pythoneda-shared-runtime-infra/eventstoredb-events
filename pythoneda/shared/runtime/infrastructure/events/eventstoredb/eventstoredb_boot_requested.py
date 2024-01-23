# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/infrastructure/events/eventstoredb/eventstoredb_boot_requested.py

This script defines the EventstoredbBootRequested class.

Copyright (C) 2024-today rydnr's pythoneda-shared-runtime-infrastructure/eventstoredb-events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared import Event
from typing import Dict, List


class EventstoredbBootRequested(Event):
    """
    Represents someone has requested EventStoreDB to be booted up.

    Class name: EventstoredbBootRequested

    Responsibilities:
        - Represent the request of booting up EventStoreDB.

    Collaborators:
        - None
    """

    def __init__(
        self,
        options: Dict,
        previousEventId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new EventstoredbBootRequested instance.
        :param options: Additional configuration.
        :type options: Dict
        :param previousEventId: The id of the previous event, if any.
        :type previousEventId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        previous_events = None
        if previousEventId:
            previous_events = [previousEventId]
        super().__init__(
            previous_events, reconstructedId, reconstructedPreviousEventIds
        )
        self._options = options

    @property
    def options(self) -> str:
        """
        Retrieves the EventStoreDB options.
        :return: Such information.
        :rtype: Dict
        """
        return self._options


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
