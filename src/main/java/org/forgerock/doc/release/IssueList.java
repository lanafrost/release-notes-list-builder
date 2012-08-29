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

public class IssueList {
    public static class Issue {
        public static class Field {
            private String _summary;

            public String getSummary() {
                return _summary;
            }

            public void setSummary(String summary) {
                _summary = summary;
            }
        }

        private String _expand;
        private String _id;
        private String _self;
        private String _key;
        private Field _fields;

        public String getExpand() {
            return _expand;
        }

        public void setExpand(String expand) {
            _expand = expand;
        }

        public String getId() {
            return _id;
        }

        public void setId(String id) {
            _id = id;
        }

        public String getSelf() {
            return _self;
        }

        public void setSelf(String self) {
            _self = self;
        }

        public String getKey() {
            return _key;
        }

        public void setKey(String key) {
            _key = key;
        }

        public Field getFields() {
            return _fields;
        }

        public void setFields(Field fields) {
            _fields = fields;
        }
    }

    private String _expand;
    private int _startAt;
    private int _maxResults;
    private int _total;
    private Issue[] _issues;

    public String getExpand() {
        return _expand;
    }

    public void setExpand(String expand) {
        _expand = expand;
    }

    public int getStartAt() {
        return _startAt;
    }

    public void setStartAt(int startAt) {
        _startAt = startAt;
    }

    public int getMaxResults() {
        return _maxResults;
    }

    public void setMaxResults(int maxResults) {
        _maxResults = maxResults;
    }

    public int getTotal() {
        return _total;
    }

    public void setTotal(int total) {
        _total = total;
    }

    public Issue[] getIssues() {
        return _issues;
    }

    public void setIssues(Issue[] issues) {
        _issues = issues;
    }

}
