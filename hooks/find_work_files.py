import sgtk
from sgtk import TankError

HookClass = sgtk.get_hook_baseclass()


class FindWorkFiles(HookClass):
    """
    Hook that can be used to filter the list of work files found by the app for the current
    Work area
    """

    def execute(self, context, work_template, version_compare_ignore_fields):
        """
        Find all work files for the specified context and work template.

        :param context:                         The context to find work files for
        :param work_template:                   The work template to match found files against
        :param version_compare_ignore_fields:   List of fields to ignore when comparing files in order to find
                                                different versions of the same file
        :returns:                               A list of file paths.
        """
        # find work files that match the current work template:
        work_fields = []
        try:
            work_fields = context.as_template_fields(work_template, validate=True)
        except TankError as e:
            # could not resolve fields from this context. This typically happens
            # when the context object does not have any corresponding objects on
            # disk / in the path cache. In this case, we cannot continue with any
            # file system resolution, so just exit early insted.
            return []

        # Build list of fields to ignore when looking for files, any missing key
        # is treated as a wildcard, which allows, for example to retrieve all files
        # for any pipeline step for a given Entity.
        skip_fields = list(version_compare_ignore_fields or [])

        # Skip any keys from work_fields that are _only_ optional in the template.  This is to
        # ensure we find as wide a range of files as possible considering all optional keys.
        # Note, this may be better as a general change to the paths_from_template method...
        skip_fields += [n for n in work_fields if work_template.is_optional(n)]

        # Find all versions so skip the 'version' key if it's present and not
        # already registered in our wildcards:
        if "version" not in skip_fields:
            skip_fields += ["version"]

        # find paths:
        work_file_paths = self.sgtk.paths_from_template(
            work_template, work_fields, skip_fields, skip_missing_optional_keys=True
        )
        return work_file_paths