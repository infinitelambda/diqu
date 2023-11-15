# Anonymous usage stats

We aim to enhance the functionality of diqu by gaining insights into user interactions. As part of this effort, we have implemented straightforward event tracking within diqu, utilizing Snowplow.

It is important to note that we do not collect credentials or any other type of private info, as we consider this information outside the scope of our interest.

The potential uses for usage statistics encompass package maintenance & future module development.

By default, event tracking is enabled. However, users of diqu can choose to opt out of this feature at any time by setting the following environment variable

  ```bash
  export DO_NOT_TRACK=true
  ```
