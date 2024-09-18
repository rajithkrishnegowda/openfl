# Copyright 2022 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import importlib


if importlib.util.find_spec("torch") is not None:
    from openfl.pipelines.eden_pipeline import EdenPipeline  # NOQA
