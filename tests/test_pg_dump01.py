#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2019-present MagicStack Inc. and the EdgeDB authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import os.path

import edgedb

from edb.testbase import server as tb


class PGDumpTestCaseMixin:

    async def ensure_schema_data_integrity(self, rawdump):
        tx = self.con.transaction()
        await tx.start()
        try:
            await self._ensure_schema_data_integrity(rawdump)
        finally:
            await tx.rollback()

    async def _ensure_schema_data_integrity(self, rawdump):
        """XXX: placeholder for data that needs checking

        SELECT * FROM "A";
        """

        print(f'AAA: {rawdump}', flush=True)


class TestPGDump01(tb.StablePGDumpTestCase, PGDumpTestCaseMixin):

    SCHEMA_DEFAULT = os.path.join(os.path.dirname(__file__), 'schemas',
                                  'pg_dump01_default.esdl')

    SETUP = os.path.join(os.path.dirname(__file__), 'schemas',
                         'pg_dump01_setup.edgeql')

    async def test_pgdump01_dump_restore(self):
        await self.check_dump_restore(
            PGDumpTestCaseMixin.ensure_schema_data_integrity)
