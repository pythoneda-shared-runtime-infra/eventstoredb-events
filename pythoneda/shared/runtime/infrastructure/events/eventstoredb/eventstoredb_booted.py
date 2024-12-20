# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/infrastructure/events/eventstoredb/eventstoredb_booted.py

This script defines the EventstoredbBooted class.

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


class EventstoredbBooted(Event):
    """
    Represents EventStoreDB has booted up.

    Class name: EventstoredbBooted

    Responsibilities:
        - Represent EventStoreDB has booted up.

    Collaborators:
        - None
    """

    def __init__(
        self,
        options: Dict,
        previousEventIds: List[str],
        reconstructedId: str = None,
    ):
        """
        Creates a new EventstoredbBooted instance.
        :param options: The EventStoreDB options.
        :type options: Dict
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(previousEventIds, reconstructedId)
        self._options = options

    @property
    def options(self) -> Dict:
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
