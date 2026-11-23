import { defineRule } from "@oxlint/plugins";

import { Declarations } from "../shared/declarations.ts";

/** [naming] Names have at most three words. */
export const nameLength = defineRule({
	create: (context) => {
		const declarations = new Declarations((node, name) => {
			const { length } = name.words;

			if (length > 3) {
				context.report({
					message: `"${name}" has ${length} words; use at most 3 (code-style: naming).`,
					node,
				});
			}
		});

		return declarations.visitors(true);
	},
	meta: {
		docs: {
			description: "[naming] Names have at most three words.",
		},
	},
});
