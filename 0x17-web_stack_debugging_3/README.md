# Web Stack Debugging #3

## Task: Strace is Your Friend

### Objective
The goal of this task is to use `strace` to identify and fix a `500 Internal Server Error` returned by Apache on a WordPress site running on a LAMP stack. Once the issue is identified, the fix should be automated using Puppet.

### Prerequisites
- Basic understanding of Linux system administration.
- Familiarity with `strace`, a diagnostic, debugging, and instructional userspace utility.
- Basic knowledge of Puppet for automation.

### Steps to Complete the Task

1. **Identify the Apache Process**:
   - Use `ps` to find the Apache process ID (PID).
     ```bash
     ps aux | grep apache2
     ```

2. **Use `strace` to Debug the Issue**:
   - Attach `strace` to the Apache process and log the output.
     ```bash
     strace -p <apache_pid> -o /tmp/apache_strace.log
     ```
   - In another terminal, trigger the error using `curl`:
     ```bash
     curl -sI 127.0.0.1
     ```
   - Analyze the `strace` output to identify the root cause of the 500 error.

3. **Fix the Issue**:
   - Based on your findings, create a Puppet manifest to fix the identified issue. For example, if the error is due to file permissions, your Puppet manifest may look like this:
     ```puppet
     file { '/var/www/html':
       ensure  => directory,
       owner   => 'www-data',
       group   => 'www-data',
       mode    => '0755',
       recurse => true,
     }

     exec { 'restart-apache':
       command => '/etc/init.d/apache2 restart',
       refreshonly => true,
       subscribe => File['/var/www/html'],
     }
     ```

4. **Apply the Puppet Manifest**:
   - Apply the manifest to implement the fix:
     ```bash
     puppet apply 0-strace_is_your_friend.pp
     ```

5. **Verify the Fix**:
   - Check if the 500 error is resolved by running:
     ```bash
     curl -sI 127.0.0.1
     ```

### Conclusion
This task demonstrated how to use `strace` for low-level debugging of a web server and how to automate a fix using Puppet. This approach is useful for identifying and resolving issues that aren't immediately apparent from logs alone.

### Repository
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x17-web_stack_debugging_3`
- File: `0-strace_is_your_friend.pp`

