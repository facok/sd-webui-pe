import contextlib

import gradio as gr
from modules import scripts, shared, script_callbacks
from modules.ui_components import FormRow, FormColumn, FormGroup, ToolButton
import json
import os
import random
from scripts.pe import PromptsExpansion

expansion = PromptsExpansion()


class PromptExpansion(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "Prompt-Expansion 1.0"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        enabled = getattr(shared.opts, "enable_Prompt_Expansion_by_default", True)
        with gr.Group():
            with gr.Accordion("Prompt-Expansion", open=enabled):
                with FormRow():
                    with FormColumn(min_width=160):
                        is_enabled = gr.Checkbox(
                            value=enabled, label="Enable Prompt-Expansion", info="GPT2-based prompt expansion as a dynamic style from Fooocus V2 ")

        return [is_enabled]

    def process(self, p, is_enabled):
        if not is_enabled:
            return


        # batchCount = len(p.all_prompts)
        # # p.all_seeds
        # if(batchCount == 1):
            # for each image in batch
        for i, prompt in enumerate(p.all_prompts):
            positivePrompt = expansion(prompt, p.all_seeds[i])
            p.all_prompts[i] = positivePrompt

        # if(batchCount > 1):
        #     styles = {}
        #     for i, prompt in enumerate(p.all_prompts):
        #         if(randomize):
        #             styles[i] = random.choice(self.styleNames)
        #         else:
        #             styles[i] = style
        #         if(allstyles):
        #             styles[i] = self.styleNames[i % len(self.styleNames)]
        #     # for each image in batch
        #     for i, prompt in enumerate(p.all_prompts):
        #         positivePrompt = createPositive(
        #             styles[i] if randomizeEach or allstyles else styles[0], prompt)
        #         p.all_prompts[i] = positivePrompt


        p.extra_generation_params["Prompt-Expansion"] = True


    def after_component(self, component, **kwargs):
        # https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/7456#issuecomment-1414465888 helpfull link
        # Find the text2img textbox component
        if kwargs.get("elem_id") == "txt2img_prompt":  # postive prompt textbox
            self.boxx = component
        # Find the img2img textbox component
        if kwargs.get("elem_id") == "img2img_prompt":  # postive prompt textbox
            self.boxxIMG = component


def on_ui_settings():
    section = ("Prompt_Expansion", "Prompt-Expansion")

    shared.opts.add_option(
        "enable_Prompt_Expansion_by_default",
        shared.OptionInfo(
            True,
            "enable Prompt-Expansion by default",
            gr.Checkbox,
            section=section
            )
    )
script_callbacks.on_ui_settings(on_ui_settings)
