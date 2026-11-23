import { defineRule } from "@oxlint/plugins";
import type { ESTree } from "@oxlint/plugins";

/**
 * [structure] A module-level constant read in only one place is written there instead.
 * Exported constants are exempt, and so are Svelte components: oxlint reads
 * only their script, so it cannot see the reads in their markup.
 */
export const singleUse = defineRule({
	create: (context) => {
		if (context.filename.endsWith(".svelte")) {
			return {};
		}

		return {
			"Program > VariableDeclaration[kind='const'] > VariableDeclarator": (
				node: ESTree.VariableDeclarator,
			) => {
				const type = node.init?.type;
				const callable = type === "ArrowFunctionExpression" || type === "FunctionExpression";

				if (node.id.type !== "Identifier" || callable) {
					return;
				}

				for (const variable of context.sourceCode.getDeclaredVariables(node)) {
					const reads = variable.references.filter((reference) => reference.isRead());

					if (reads.length === 1) {
						context.report({
							message: `"${variable.name}" is used once; write it where it is used (code-style: structure).`,
							node: node.id,
						});
					}
				}
			},
		};
	},
	meta: {
		docs: {
			description: "[structure] No module-level constants that are read only once.",
		},
	},
});
