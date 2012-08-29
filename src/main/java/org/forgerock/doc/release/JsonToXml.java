/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * If applicable, add the following below this MPL 2.0 HEADER, replacing
 * the fields enclosed by brackets "[]" replaced with your own identifying
 * information:
 *     Portions Copyright [yyyy] [name of copyright owner]
 *
 *     Copyright 2012 ForgeRock AS
 *
 */
package org.forgerock.doc.release;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

import org.codehaus.jackson.map.ObjectMapper;

public final class JsonToXml {

    /**
     * Transform JSON object from JIRA into DocBook 5 &lt;itemizedlist&gt;.
     *
     * The current implementation is very brittle, relying on the object
     * returned by a JIRA query that returns a list of issues with only
     * their summaries (and so the JSON matches the IssueList object).
     *
     * @param args JIRA URL to GET JSON object. For example:
     * "http://bugster.forgerock.org/jira/rest/api/2/search?jql=project+%3D+OPENDJ+AND+fixVersion+%3D+%222.5.0%22+AND+component+%21%3D+documentation+AND+type+%3D+Bug+and+resolution+%3D+Fixed+and+priority+%21%3D+Trivial&startAt=0&maxResults=200&fields=summary"
     * or
     * "http://bugster.forgerock.org/jira/rest/api/2/search?jql=project+%3D+OpenDJ+and+affectedVersion+%3D+%222.5.0%22+and+(resolution+%3D+Unresolved+or+(resolution+%3D+fixed+and+fixVersion+!%3D+%222.5.0%22))+and+component+!%3D+documentation+and+type+%3D+Bug&startAt=0&maxResults=200&fields=summary"
     */
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Specify a JIRA query URL as an argument.");
            System.exit(-1);
        }

        try {
            URL jiraURL = new URL(args[0]);
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(jiraURL.openStream()));

            ObjectMapper mapper = new ObjectMapper();
            IssueList issues = mapper.readValue(in, IssueList.class);

            System.out.println("  <itemizedlist>");
            String prefix = "   <listitem><para><link xlink:show=\"new\" "
                    + "xlink:href=\"https://bugster.forgerock.org/jira/browse/";
            String suffix = "</para></listitem>";
            for (IssueList.Issue issue : issues.getIssues()) {
                String bugId = issue.getKey();
                IssueList.Issue.Field field = issue.getFields();
                String summary = field.getSummary();

                String infix = bugId + "\">"+ bugId + "</link>: " + summary;
                System.out.println(prefix + infix + suffix);
            }
            System.out.println("  </itemizedlist>");
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private JsonToXml() {
        // Not used.
    }
}
