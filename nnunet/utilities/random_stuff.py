#    Copyright 2020 Division of Medical Image Computing, German Cancer Research Center (DKFZ), Heidelberg, Germany
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


from typing import Tuple
from nnunet.paths import default_plans_identifier, default_cascade_trainer, default_trainer


class no_op(object):
    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass


def get_default_trainer_planer_name(model: str) -> Tuple[str, str]:
    if model == "3d_cascade_fullres":
        trainer = default_cascade_trainer
    elif model.startswith("TransUNet"):
        trainer = "TransUNetTrainer"
    else:
        trainer = default_trainer
    
    if model == "TransUNet2D":
        planner = "nnUNetPlans_transUNet"
    else:
        planner = default_plans_identifier
    return (trainer, planner)
